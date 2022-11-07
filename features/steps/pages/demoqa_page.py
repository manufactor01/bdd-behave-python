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

    def get_current_address_textarea(self):
        return self.driver.find_element(By.ID, 'currentAddress')

    def get_permanent_address_textarea(self):
        return self.driver.find_element(By.ID, 'permanentAddress-wrapper')

    def get_submit_btn(self):
        return self.driver.find_element(By.ID, 'submit')
