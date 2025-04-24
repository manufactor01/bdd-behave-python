from behave import given, when, then

from features.pages.saucedemo_page import SauceDemoPage

@given('I am on the SauceDemo login page')
def step_impl(context):
    context.page = SauceDemoPage(context.driver, context.config["saucedemo"]["url"])
    context.page.load()
    assert context.page.is_on_login_page(), "Not on the SauceDemo login page"

@when('I enter with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.page.login(username, password)
    
@then('I should be redirected to the inventory page')
def step_impl(context):
    assert context.page.is_on_inventory_page(), "Not on the SauceDemo inventory page"


@then('I should see an error message')
def step_impl(context):
    assert context.page.is_on_login_page(), "Not on the SauceDemo login page"
    assert context.page.get_error_message() is not None, "No error message displayed"
    assert context.page.get_error_message() == context.config["saucedemo"]["error_message"] , "Incorrect message displayed"