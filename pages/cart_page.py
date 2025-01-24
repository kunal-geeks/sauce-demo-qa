from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait import wait_for_element_to_be_clickable

class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    REMOVE_BUTTON = (By.CSS_SELECTOR, "[data-test^='remove-']")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "[data-test='checkout']")
    CART_ITEMS = (By.XPATH, "//div[@class='cart_item_label']//a")

    # Actions
    def remove_from_cart(self, product_id):
        try:
            # Locate the product name based on the product ID
            product_name_element = self.driver.find_element(By.ID, f"item_{product_id}_title_link")
            product_name = product_name_element.find_element(By.CSS_SELECTOR, "div.inventory_item_name").text
        
            # Transform the product name: lowercase and replace spaces with hyphens
            product_name_slug = product_name.lower().replace(" ", "-")
        
            # Locate the 'Remove' button using the transformed product name
            remove_button = self.driver.find_element(By.ID, f"remove-{product_name_slug}")
        
            # Wait for the 'Remove' button to be clickable and click it
            wait_for_element_to_be_clickable(self.driver, remove_button)
            remove_button.click()
            self.logger.info(f"Product '{product_name}' removed from the cart.")
        
        except Exception as e:
            self.logger.error(f"Error removing product '{product_id}' from the cart: {e}")
            raise e

    def get_cart_items(self):
        """
        Returns all items present in the cart.
        :return: A list of cart item elements.
        """
        return self.driver.find_elements(*self.CART_ITEMS)

    def click_checkout(self):
        """
        Clicks the checkout button to proceed to checkout.
        """
        checkout_button = self.driver.find_element(*self.CHECKOUT_BUTTON)
        wait_for_element_to_be_clickable(self.driver, checkout_button)
        checkout_button.click()

    def is_item_present(self, product_id):
        """
        Verifies if a specific item is present in the cart based on its product ID.
        :param product_id: The product ID (e.g., 0,1,2,3,4,5).
        :return: True if the item is present, False otherwise.
        """
        try:
            # Transform the product ID into a slug (lowercase and spaces replaced with hyphens)
            product_slug = f"item_{product_id}_title_link"

            # Check if the item is present in the cart by looking for its corresponding element
            cart_items = self.driver.find_elements(*self.CART_ITEMS)
            for item in cart_items:
                if product_slug in item.get_attribute("id"):
                    self.logger.info(f"Item with ID '{product_id}' is present in the cart.")
                    return True

            self.logger.warning(f"Item with ID '{product_id}' is not found in the cart.")
            return False

        except Exception as e:
            self.logger.error(f"Error checking if item '{product_id}' is in the cart: {e}")
            raise e
