from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.wait import wait_for_element_to_be_visible
from pages.base_page import BasePage


class HeaderComponent(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    LOGIN_BUTTON = (By.ID, "login-button")  # Locator for the login button

    # Actions
    def logout(self):
        """
        Logs out the user if logged in. Handles already logged-out cases gracefully.
        """
        try:
            self.logger.info("Attempting to perform logout.")

            # Check if the user is already logged out
            if self.is_logged_out():
                self.logger.info("User is already logged out. No action needed.")
                return

            # Wait for the menu button to be visible and click it
            self.logger.info("Locating the menu button.")
            wait_for_element_to_be_visible(self.driver, self.MENU_BUTTON)
            self.driver.find_element(*self.MENU_BUTTON).click()
            self.logger.info("Menu button clicked.")

            # Wait for the logout link to be visible and click it
            self.logger.info("Locating the logout link.")
            wait_for_element_to_be_visible(self.driver, self.LOGOUT_LINK)
            self.driver.find_element(*self.LOGOUT_LINK).click()
            self.logger.info("Logout link clicked. User logged out successfully.")

        except TimeoutException as e:
            self.logger.error(f"Logout process failed: {str(e)}")
            raise Exception("Unable to complete the logout process.")

    def is_logged_out(self):
        """
        Verifies if the user is logged out by checking the visibility of the login button.
        """
        try:
            self.logger.info("Checking if the user is logged out.")
            wait_for_element_to_be_visible(self.driver, self.LOGIN_BUTTON)
            self.logger.info("Login button is visible. User is logged out.")
            return True
        except TimeoutException:
            self.logger.info("Login button is not visible. User is logged in.")
            return False
