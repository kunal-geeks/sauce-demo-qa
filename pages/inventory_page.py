from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages.base_page import BasePage
from utils.wait import wait_for_element_to_be_clickable, wait_for_element_to_be_present, wait_for_element_to_be_visible

class InventoryPage(BasePage):
    # Locators for elements on the inventory page
    PRODUCT_LIST = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    SORT_SELECT = (By.CLASS_NAME, "product_sort_container")
    ACTIVE_OPTION = (By.CLASS_NAME, "active_option")
    CART_ICON = (By.CSS_SELECTOR, "a.shopping_cart_link")
    CART_TITLE = (By.CSS_SELECTOR, "span.title[data-test='title']") 
    
    def __init__(self, driver):
        super().__init__(driver)

    def is_product_displayed(self, product_name):
        """Verifies if a product is displayed on the inventory page."""
        try:
            # Wait for the product list to be present and visible
            wait_for_element_to_be_present(self.driver, self.PRODUCT_LIST)
            wait_for_element_to_be_visible(self.driver, self.PRODUCT_LIST)
            
            # Get all product names on the page
            products = self.driver.find_elements(*self.PRODUCT_NAME)
            
            # Check if the product is in the list
            for product in products:
                if product_name.lower() in product.text.lower():
                    self.logger.info(f"Product '{product_name}' is displayed on the page.")
                    return True

            # If the product is not found
            self.logger.warning(f"Product '{product_name}' is not displayed on the page.")
            return False

        except NoSuchElementException as e:
            self.logger.error(f"Error occurred while checking if product '{product_name}' is displayed: {str(e)}")
            raise Exception(f"Error occurred while checking if product '{product_name}' is displayed: {str(e)}")
        except TimeoutException as e:
            self.logger.error(f"Timeout occurred while checking if product '{product_name}' is displayed: {str(e)}")
            raise Exception(f"Timeout occurred while checking if product '{product_name}' is displayed: {str(e)}")
        except Exception as e:
            self.logger.error(f"Unexpected error occurred: {str(e)}")
            raise Exception(f"Unexpected error occurred: {str(e)}")

    def sort_products(self, sort_type):
        """Sorts products by the given sort type."""
        try:
            # Wait for the sort container to be visible
            wait_for_element_to_be_visible(self.driver, self.SORT_SELECT)
            
            # Click the sort dropdown and select the sort type
            sort_select = self.driver.find_element(*self.SORT_SELECT)
            sort_select.click()
            options = sort_select.find_elements(By.TAG_NAME, "option")
            
            # Select the desired sort option
            for option in options:
                if option.text == sort_type:
                    option.click()
                    self.logger.info(f"Products sorted by '{sort_type}'.")
                    return True

            self.logger.warning(f"Sort option '{sort_type}' not found.")
            return False
        except NoSuchElementException as e:
            self.logger.error(f"Error occurred while sorting products: {str(e)}")
            raise Exception(f"Error occurred while sorting products: {str(e)}")
        except TimeoutException as e:
            self.logger.error(f"Timeout occurred while sorting products: {str(e)}")
            raise Exception(f"Timeout occurred while sorting products: {str(e)}")
        except Exception as e:
            self.logger.error(f"Unexpected error occurred: {str(e)}")
            raise Exception(f"Unexpected error occurred: {str(e)}")


    def add_to_cart(self, product_id):
        """
        Adds a specific product to the cart by its ID.
        :param product_id: The product ID (e.g., 0,1,2,3,4,5).
        """
        try:
            # Locate the product name based on the product ID
            product_name_element = self.driver.find_element(By.ID, f"item_{product_id}_title_link")
            product_name = product_name_element.find_element(By.CSS_SELECTOR, "div.inventory_item_name").text
        
            # Transform the product name: lowercase and replace spaces with hyphens
            product_name_slug = product_name.lower().replace(" ", "-")
        
            # Locate the 'Add to Cart' button using the transformed product name
            add_to_cart_button = self.driver.find_element(By.ID, f"add-to-cart-{product_name_slug}")

            # If the 'Add to Cart' button text is 'Remove from Cart', it means the item is already in the cart
            if add_to_cart_button.text.lower() == "remove":
                self.logger.info(f"Product '{product_name}' is already in the cart. No need to add it again.")
                return

            # Wait for the 'Add to Cart' button to be clickable and click it
            wait_for_element_to_be_clickable(self.driver,add_to_cart_button)
            add_to_cart_button.click()
        
        except Exception as e:
            self.logger.error(f"Error adding product '{product_id}' to the cart: {e}")
            raise e

    def go_to_cart(self):
        """
        Navigates to the cart page by clicking on the cart icon.
        """
        try:
            cart_icon = wait_for_element_to_be_clickable(self.driver, self.CART_ICON)
            cart_icon.click()
            self.logger.info("Navigated to the cart page successfully.")
            # Wait for the 'Your Cart' title to be visible after navigation
            
            wait_for_element_to_be_visible(self.driver, self.CART_TITLE)
            self.logger.info("Cart page loaded and 'Your Cart' title is visible.")
        
        except Exception as e:
            self.logger.error(f"Error navigating to the cart page: {e}")
            raise