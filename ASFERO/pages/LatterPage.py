from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By


class MailLocators:
    LOCATOR_ENTER_EMAIL = (By.XPATH, '//*[@id="to"]')
    LOCATOR_ENTER_SUBJECT = (By.XPATH, '/html/body/div[4]/div[6]/div[1]/div[1]/div[1]/div/form/div[5]/div[2]/span/input[1]')
    LOCATOR_ENTER_TEXT_OF_LETTER = (By.CSS_SELECTOR, '.text_editor_browser textarea')
    LOCATOR_CLICK_ON_THE_BUTTON_SEND = (By.CSS_SELECTOR, '.send_container input.bold')
    LOCATOR_ON_THE_BUTTON_LETTERS = (By.CSS_SELECTOR, '/html/body/div[2]/div[5]/ul/li[2]')


class AddLetterPage(BasePage):

    def enter_email(self, email: str):
        time.sleep(2)
        email_field = self.find_element(MailLocators.LOCATOR_ENTER_EMAIL)
        #email_field.click()
        time.sleep(2)
        email_field.send_keys(email)

    def enter_subject(self, subject: str):
        time.sleep(2)
        subject_field = self.find_element(MailLocators.LOCATOR_ENTER_SUBJECT)
        #subject_field.click()
        time.sleep(2)
        subject_field.send_keys(subject)

    def enter_text_of_letter(self, text: str):
        time.sleep(3)
        text_field = self.find_element(MailLocators.LOCATOR_ENTER_TEXT_OF_LETTER)
        #text_field.click()
        time.sleep(3)
        text_field.send_keys(text)

    def click_on_the_button_send(self):
        time.sleep(2)
        button_send = self.find_element(MailLocators.LOCATOR_CLICK_ON_THE_BUTTON_SEND)
        time.sleep(2)
        button_send.click()

    def click_on_the_button_letters(self):
        self.go_to_letter_page()


    def send_the_last_masseges(self):
        self.go_to_control_folder_ms()
        self.click_on_the_button_delete_ms()

        self.go_to_letter_site()
        list_of_ms = self.creting_the_last_messages()
        text_field = self.find_element(MailLocators.LOCATOR_ENTER_TEXT_OF_LETTER)
        for message in list_of_ms:
            text_field.send_keys(message, "\n")


