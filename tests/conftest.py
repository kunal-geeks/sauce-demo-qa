import pytest
from selenium import webdriver
from pages.header_component import HeaderComponent
from pages.inventory_page import InventoryPage
from utils.config_reader import get_config
from utils.logger import get_logger
from utils.screenshots import take_screenshot

logger = get_logger()

@pytest.fixture(scope="session")
def config():
    return get_config()

# Pytest hook to capture test result and take screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Get the test result
    outcome = yield
    report = outcome.get_result()

    # Check if the test failed
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")  # Get the driver instance
        if driver:
            screenshot_path = take_screenshot(driver, item.name)
            # Log the screenshot location after failure
            logger.error(f"Test failed: {item.name}. Screenshot saved to {screenshot_path}")

@pytest.fixture(scope="function")
def driver(config):
    browser = config["browser"]
    options = webdriver.ChromeOptions()
    if config["headless"]:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(config["environment"])
    yield driver
    driver.quit()

@pytest.fixture
def inventory_page(driver):
    return InventoryPage(driver)

@pytest.fixture
def header_component(driver):
    """
    Fixture to initialize the HeaderComponent for the test.
    """
    return HeaderComponent(driver)