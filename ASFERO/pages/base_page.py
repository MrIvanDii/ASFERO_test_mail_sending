import time
import sqlite3
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.i.ua/"
        self.letter_url = "https://mbox2.i.ua/compose/1525287940/"
        self.failed_message = 'Mail delivery failed: returning message to sender'
        self.base_letter_url = 'https://mbox2.i.ua'
        self.LINK_ON_THE_BUTTON_LETTERS = 'https://mbox2.i.ua/?_rand=1540247200'
        self.LINK_ON_THE_FOLDER_MS = 'https://mbox2.i.ua/settings/folders/?_rand=1708605522'
        self.LINK_FOR_DELETING_ALL_MS = 'https://mbox2.i.ua/settings/folders/?folder=INBOX&clear=1&_rand=1708679207&SSG=99852d47'
        self.conn = sqlite3.connect('DB/db.sqlite')
        self.cur = self.conn.cursor()


    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        self.driver.get(self.base_url)

    def go_to_control_folder_ms(self):
        time.sleep(3)
        self.driver.get(self.LINK_FOR_DELETING_ALL_MS)

    def go_to_letter_site(self):
        time.sleep(2)
        self.driver.get(self.letter_url)
        time.sleep(2)

    def go_to_letter_page(self):
        time.sleep(2)
        self.driver.get(self.LINK_ON_THE_BUTTON_LETTERS)

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def get_source_of_page(self):
        time.sleep(3)
        with open('HTML/page.html', "w") as file:
            file.write(self.driver.page_source)

    def get_source_of_page_with_letters(self):
        time.sleep(3)
        with open('HTML/page2.html', "w") as file:
            file.write(self.driver.page_source)

    def check_the_status(self):
        with open("HTML/page2.html", "rb") as file:
            src = file.read().decode(errors='replace')

        soup = BeautifulSoup(src, "lxml")
        status = soup.find("div", class_="messages").find("form").find_all('span', class_='sbj')
        all_ms_status = [ms.text for ms in status]
        failed_delivery = 'Mail delivery failed: returning message to sender'

        summery_of_failes = []
        for status in all_ms_status:
            if status == failed_delivery:
                summery_of_failes.append(1)

        if sum(summery_of_failes) < 1:
            print(f"Succesful messages delivery")

        elif sum(summery_of_failes) > 1:
            print(f"We got only {sum(summery_of_failes)} failed trys of mail sending")


    def collect_data_head(self):
        with open("HTML/page.html", "rb") as file:
            src = file.read().decode(errors='replace')

        soup = BeautifulSoup(src, "lxml")
        status = soup.find("div", class_="messages").find("form").find_all('span', class_='sbj')
        all_ms_status = [ms.text for ms in status]

        self.cur.executescript("""
                                DROP TABLE IF EXISTS data_head;
                                CREATE TABLE data_head (
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                comment TEXT
                                )
                                """)
        self.conn.commit()

        for status in all_ms_status:
            self.cur.execute("INSERT INTO data_head (comment) VALUES(?)", (status,))
        self.conn.commit()

    def collect_links_messages(self):
        with open("HTML/page.html", "rb") as file:
            src = file.read().decode(errors='replace')

        dom = 'https://mbox2.i.ua'
        soup = BeautifulSoup(src, "lxml")
        status = soup.find("div", class_="messages").find("form").find_all('a')
        urls = [dom + a['href'] for a in status]

        self.cur.executescript("""
                                DROP TABLE IF EXISTS data_urls;
                                CREATE TABLE data_urls (
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                comment TEXT
                                )
                                """)
        self.conn.commit()

        for url in urls:
            self.cur.execute("INSERT INTO data_urls (comment) VALUES(?)", (url,))
            self.conn.commit()

    def collect_body_message(self):
        self.cur.execute("""SELECT comment FROM data_urls""")
        data = self.cur.fetchall()
        urls_list = [i[0] for i in data]

        self.cur.executescript("""
                                DROP TABLE IF EXISTS data_body;
                                CREATE TABLE data_body (
                                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                comment TEXT
                                )
                                """)
        self.conn.commit()

        for url in urls_list:
            time.sleep(3)
            self.driver.get(url)
            time.sleep(3)

            src = self.driver.page_source
            soup = BeautifulSoup(src, "lxml")
            body_text = soup.find("div", class_="message_body").find("pre").text

            self.cur.execute("INSERT INTO data_body (comment) VALUES(?)", (body_text,))
            self.conn.commit()

    def creting_the_last_messages(self):
        self.cur.execute("""
                    SELECT data_head.comment, data_body.comment, data_urls.comment
                    FROM data_head
                    LEFT JOIN data_body, data_urls
                    ON data_head.id=data_body.id=data_urls.id
                    """)
        data = self.cur.fetchall()

        messeges_list = []
        for i in data:
            theme = i[0]
            body = i[1]
            count_of_numbers_in_body = sum([1 for char in body if char.isdigit()])
            count_of_alpha_in_body = sum([1 for char in body if char.isalpha()])

            new_message = f"Received mail on theme {theme} with message: {body}. It contains {count_of_alpha_in_body} letters and {count_of_numbers_in_body} numbers"
            messeges_list.append(new_message)

        return messeges_list


    def click_on_the_button_delete_ms(self):

        src = self.driver.page_source
        soup = BeautifulSoup(src, "lxml")
        uri = soup.find("span", class_="function").find("a")['href']
        url = f"{self.base_letter_url}{uri}"
        time.sleep(2)
        self.driver.get(url)
        time.sleep(3)
