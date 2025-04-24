import allure
from allure_commons.types import AttachmentType
from utils.driver_utils import read_config, prepare_driver

def before_all(context):
    context.config = read_config()

def before_scenario(context, scenario):
    browser = context.config["duckduckgo"].get("browser", "firefox")
    context.driver = prepare_driver(browser)

def after_step(context, step):
    if hasattr(context, 'driver'):
        name = f"{step.keyword.strip()} - {step.name}"
        allure.attach(
            context.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=AttachmentType.PNG
        )
    
def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        context.driver.quit()