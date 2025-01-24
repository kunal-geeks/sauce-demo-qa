from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_for_element_to_be_visible, wait_for_element_to_be_clickable

class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        """
        Initializes the CheckoutCompletePage with the given WebDriver instance.
        :param driver: WebDriver instance.
        """
        super().__init__(driver)

    # Locators
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    BACK_HOME_BUTTON = (By.LINK_TEXT, "Back Home")

    def verify_order_completion_message(self):
        """
        Verifies the order completion message on the page.
        :return: True if the message is correct, otherwise raises an AssertionError.
        """
        try:
            header = wait_for_element_to_be_visible(self.driver, self.COMPLETE_HEADER)
            assert "Thank you for your order!" in header.text, "Order completion message is incorrect!"
            self.logger.info("Order completion message verified successfully.")
            return True
        except AssertionError as e:
            self.logger.error(f"Order completion message verification failed: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error while verifying order completion message: {e}")
            raise

    def navigate_back_home(self):
        """
        Clicks the 'Back Home' button to navigate to the home page.
        """
        try:
            back_home_button = wait_for_element_to_be_clickable(self.driver, self.BACK_HOME_BUTTON)
            back_home_button.click()
            self.logger.info("Navigated back to the home page successfully.")
        except Exception as e:
            self.logger.error(f"Error while navigating back home: {e}")
            raise
