from pages.page import Page 
from selenium.webdriver.common.by import By
import time

class DemoQAPage(Page):

    def __init__(self, driver, time_sleep):
        super().__init__(driver, time_sleep)
        self.url = 'https://demoqa.com/text-box'
        self.time_sleep = int(time_sleep)

    def open_page(self):
        self.search_page(self.url)

    def get_fullname_input(self):
        return self.driver.find_element(By.ID, 'userName')

    def get_email_input(self):
        return self.driver.find_element(By.ID, 'userEmail')

    def get_current_address_input(self):
        return self.driver.find_element(By.ID, 'currentAddress')

    def get_permanent_address_input(self):
        return self.driver.find_element(By.ID, 'permanentAddress-wrapper')

    def get_submit_btn(self):
        return self.driver.find_element(By.ID, 'submit')

    def complete_form(self, data):
        fullname_input = self.get_fullname_input()
        email_input = self.get_email_input()
        current_address_input = self.get_current_address_input()
        permanent_address_input = self.get_permanent_address_input()

    def submit_form(self):
        # self.get_submit_btn().click()
        pass
