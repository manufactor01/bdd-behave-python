import time
from selenium.webdriver.common.by import By

class Page:

    def __init__(self, driver, time_sleep):
        self.driver = driver
        self.time_sleep = time_sleep
        self.folder_name = "screenshots/"
        self.img_extension = ".png"

    def close_driver(self):
        self.driver.close()

    def search_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(self.time_sleep)

    def generate_screenshot(self, filename):
        this.driver.save_screenshot(self.folder_name + filename + self.img_extension)
