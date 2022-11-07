import configparser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path

def read_config():
    config = configparser.ConfigParser()
    config.read('../../config.ini')
    return config

def prepare_driver_for_chrome():
    service_object = Service(binary_path)
    driver = webdriver.Chrome(service=service_object)
    return driver

def prepare_driver_for_docker():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options)

    return driver

def prepare_driver(driver_type):
    driver = None

    if driver_type == "chrome": 
        driver = prepare_driver_for_chrome()

    if driver_type == "docker":
        driver = prepare_driver_for_docker()

    print("Driver is ready...")

    return driver
