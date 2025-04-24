from behave import given, when, then
from features.pages.duckduckgo_page import DuckDuckGoPage
import allure
from allure_commons.types import AttachmentType

@given('I am on the DuckDuckGo homepage')
def step_impl(context):
    context.page = DuckDuckGoPage(context.driver, context.config["duckduckgo"]["url"])
    context.page.load()

@when('I search for the configured term')
def step_impl(context):
    term = context.config["duckduckgo"]["search_term"]
    context.page.search(term)

@then('I should see results related to the search term')
def step_impl(context):
    term = context.config["duckduckgo"]["search_term"]
    results = context.page.get_result_texts()
    try:
        assert any(term.lower() in text.lower() for text in results), "No result contains the search term"
    except AssertionError as e:
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name="Search Results",
            attachment_type=AttachmentType.PNG
        )
        raise e