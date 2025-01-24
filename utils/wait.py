from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_to_be_present(driver, by, timeout=20):
    """Waits for an element to be present in the DOM."""
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(by))

def wait_for_element_to_be_visible(driver, by, timeout=20):
    """Waits for an element to be visible on the page."""
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(by))

def wait_for_element_to_be_clickable(driver, by, timeout=20):
    """Waits for an element to be clickable."""
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(by))
