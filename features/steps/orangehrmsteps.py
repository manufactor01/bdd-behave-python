from behave import *
from selenium import webdriver
from pages.orangehrm_page import OrangeHrmPage
import helper

@given('launch chrome browser')
def launchBrowser(context):
    config = helper.read_config()
    time_sleep = config['Settings']['time_sleep']
    driver_type = config['Settings']['driver']
    driver = helper.prepare_driver(driver_type)

    context.orangehrm_page = OrangeHrmPage(driver, time_sleep)


@when('open orange hrm homepage')
def openHomePage(context):
    print("Open Home Page")
    # raise NotImplementedError(u'STEP: When open orange hrm homepage')


@then('verify that the logo present on page')
def verifyLogo(context):
    print("Verify Logo")
    # raise NotImplementedError(u'STEP: Then verify that the logo present on page')


@then('close browser')
def closeBrowser(context):
    # raise NotImplementedError(u'STEP: Then close browser')
    context.orangehrm_page.close_driver()
