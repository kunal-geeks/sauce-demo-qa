from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import get_logger

class BasePage:
    
    def __init__(self, driver):
        """
        Base page constructor to initialize the WebDriver and logger.

        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def find_element(self, locator, value):
        """
        Find a single element on the page.

        :param locator: Locator strategy (e.g., By.ID, By.XPATH).
        :param value: Value for the locator strategy.
        :return: WebElement instance if found, else None.
        """
        try:
            self.logger.debug(f"Attempting to find element: Locator={locator}, Value={value}")
            element = self.driver.find_element(locator, value)
            self.logger.info(f"Element found: Locator={locator}, Value={value}")
            return element
        except Exception as e:
            self.logger.error(f"Error finding element: Locator={locator}, Value={value}. Exception: {e}")
            raise

    # Other methods like click_element, send_keys_to_element, etc., can follow the same pattern

