from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

class DuckDuckGoPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.search_input = (By.ID, "searchbox_input")
        self.result_links = (By.CSS_SELECTOR, "a.result__a")

    def load(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def search(self, term):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header_headerContent__LYxh6")))
        
        search_box = self.driver.find_element(*self.search_input)
        search_box.send_keys(term + Keys.RETURN)
        time.sleep(2)

    def get_result_texts(self):
        elements = self.driver.find_elements(*self.result_links)
        return [el.text for el in elements]
