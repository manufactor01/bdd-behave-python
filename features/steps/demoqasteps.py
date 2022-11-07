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
    fullname_input = context.demoqa_page.get_fullname_input()
    email_input = context.demoqa_page.get_email_input()
    current_address_textarea = context.demoqa_page.get_current_address_textarea()
    permanet_address_textarea = context.demoqa_page.get_permanent_address_textarea()
    submit_btn = context.demoqa_page.get_submit_btn()

    fullname_input.sendKeys("Kevin Mitnick")
    email_input.sendKeys("kmitnick@sec.org")


@then(u'se registraron datos en demoqa')
def checkRegisteredData(context):
    # raise NotImplementedError(u'STEP: Then se registraron datos en demoqa')
    context.demoqa_page.close_driver()
