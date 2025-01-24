from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[data-test='continue']")

    # Actions
    def fill_checkout_information(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ZIP_CODE).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
