from behave import *
from selenium import webdriver
from pages.demoqa_page import DemoQAPage

import helper

@given('acceder a pagina demoqa')
def openPage(context):
    config = helper.read_config()
    time_sleep = config['Settings']['time_sleep']
    driver_type = config['Settings']['driver']
    driver = helper.prepare_driver(driver_type)

    context.demoqa_page = DemoQAPage(driver, time_sleep)
    context.demoqa_page.open_page()

@when(u'ingresar datos en textbox')
def completeTextboxData(context):
    data = {
            "fullname": "Kevin Mitnick",
            "email": "kmitnick@security.org",
            "currentAddress": "nueva data",
            "permanentAddress": "vieja data forever"
            }

    context.demoqa_page.complete_form(data)
    # context.demoqa_page.submit_form()

@then(u'se registraron datos en demoqa')
def checkRegisteredData(context):
    # raise NotImplementedError(u'STEP: Then se registraron datos en demoqa')
    context.demoqa_page.close_driver()
