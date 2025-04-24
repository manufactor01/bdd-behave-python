from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SauceDemoPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.inventory_page = (By.CLASS_NAME, "inventory_list")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")
    
    def load(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def login(self, username, password):
        self.wait_for_element(self.username_input)
        
        username_field = self.driver.find_element(*self.username_input)
        password_field = self.driver.find_element(*self.password_input)
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        self.take_screenshot("login.png")
        self.driver.find_element(*self.login_button).click()

    def wait_for_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def is_on_login_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.username_input))
            return True
        except:
            return False

    def is_on_inventory_page(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.inventory_page))
            return True
        except:         
            return False

    def get_error_message(self):
        try:
            self.wait_for_element(self.error_message)
            return self.driver.find_element(*self.error_message).text
        except:
            return None
    

    def wait_for_page_to_load(self):    
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.inventory_page))

    def take_screenshot(self, filename):
        self.driver.save_screenshot(filename)
        print(f"Screenshot saved as {filename}")

    def quit(self):
        self.driver.quit()
        print("Driver quit successfully")