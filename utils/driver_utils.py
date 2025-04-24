import configparser
from selenium import webdriver
import geckodriver_autoinstaller

def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def prepare_driver_for_firefox():
    geckodriver_autoinstaller.install()
    return webdriver.Firefox()

def prepare_driver(driver_type):
    if driver_type == "firefox":
        return prepare_driver_for_firefox()
    else:
        raise ValueError(f"Unsupported driver_type: {driver_type}")

def close_driver(driver):
    driver.quit()