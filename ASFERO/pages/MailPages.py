import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class MailLocators:
    LOCATOR_MAIL_LOGIN = (By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[2]/div[1]/div[3]/form/ul/li[1]/p[2]/input')
    LOCATOR_MAIL_PASSWORD = (By.XPATH, '/html/body/div[3]/div[3]/div[3]/div[2]/div[1]/div[3]/form/ul/li[1]/input')

class LogInPage(BasePage):


    def enter_login(self, email_name: str):
        time.sleep(4)
        login_field = self.find_element(MailLocators.LOCATOR_MAIL_LOGIN)
        login_field.click()
        login_field.send_keys(email_name)


    def enter_password_and_return(self, pass_name: str):
        pass_field = self.find_element(MailLocators.LOCATOR_MAIL_PASSWORD)
        pass_field.click()
        pass_field.send_keys(pass_name)
        time.sleep(2)
        pass_field.send_keys(Keys.RETURN)