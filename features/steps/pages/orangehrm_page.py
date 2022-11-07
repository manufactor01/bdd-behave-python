from pages.page import Page 
from selenium.webdriver.common.by import By

class OrangeHrmPage(Page):
    def __init__(self, driver, time_sleep):
        super().__init__(driver, time_sleep)
        self.url = 'https://demoqa.com/text-box'

    def get_fullname_input(self):
        return self.driver.find_element(By.XPATH, '')

    def get_email_input(self):
        return self.driver.find_element(By.XPATH, '')

    def get_current_address_textarea(self):
        return self.driver.find_element(By.XPATH, '')

    def get_permanent_address_textarea(self):
        return self.driver.find_element(By.XPATH, '')

    def get_submit_btn(self):
        return self.driver.find_element(By.XPATH, '')
