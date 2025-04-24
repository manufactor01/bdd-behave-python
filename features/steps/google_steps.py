from behave import given, then
from features.pages.google_page import GooglePage
from utils.driver_utils import prepare_driver

driver = None
google_page = None

@given('I open the Google homepage')
def step_impl(context):
    global driver, google_page
    driver = prepare_driver("chrome")
    google_page = GooglePage(driver)
    google_page.load()

@then('the title should be "{expected_title}"')
def step_impl(context, expected_title):
    assert google_page.get_title() == expected_title
    driver.quit()
