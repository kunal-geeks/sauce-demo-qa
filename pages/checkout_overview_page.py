from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BUTTON = (By.CSS_SELECTOR, "[data-test='finish']")

    # Actions
    def verify_totals(self, expected_item_total, expected_tax, expected_total):
        item_total = self.driver.find_element(*self.ITEM_TOTAL).text
        tax = self.driver.find_element(*self.TAX).text
        total = self.driver.find_element(*self.TOTAL).text

        assert expected_item_total in item_total, "Item total mismatch"
        assert expected_tax in tax, "Tax mismatch"
        assert expected_total in total, "Total mismatch"

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()
