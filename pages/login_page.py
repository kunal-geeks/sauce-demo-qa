from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    LOGIN_BUTTON = (By.ID, "login-button")
    def __init__(self, driver):
        # Call the parent class constructor
        super().__init__(driver)

    def login(self, username, password):
        try:
            self.logger.info("Attempting to log in with provided credentials.")
            # Example actions
            self.find_element(By.ID, "user-name").send_keys(username)
            self.find_element(By.ID, "password").send_keys(password)
            self.find_element(By.ID, "login-button").click()
            self.logger.info("Login action performed successfully.")
        except Exception as e:
            self.logger.error(f"Error during login: {e}")
            raise

    def is_login_button_displayed(self):
        return self.driver.find_element(*self.LOGIN_BUTTON).is_displayed()
