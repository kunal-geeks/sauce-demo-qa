import pytest
import allure
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

@allure.feature("Inventory Tests")
@allure.story("Product Display Verification")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("product_name", ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", 
                                         "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"])
def test_product_display(driver, product_name):
    """Test to verify if products are displayed correctly on the inventory page."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    
    try:
        # Verify if the product is displayed on the page
        is_displayed = inventory_page.is_product_displayed(product_name)
        
        assert is_displayed, f"{product_name} is not displayed on the inventory page."
        
        allure.attach(driver.get_screenshot_as_png(), name=f"product_display_{product_name}", attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name=f"product_display_error_{product_name}", attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed for {product_name}: {str(e)}")

@allure.feature("Inventory Tests")
@allure.story("Product Sorting")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("sort_type", ["Price (high to low)", "Price (low to high)", "Name (A to Z)", "Name (Z to A)"])
def test_product_sorting(driver, sort_type):
    """Test to verify if products are sorted correctly on the inventory page."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page = InventoryPage(driver)
    
    try:
        # Sort products by the given sort type
        is_sorted = inventory_page.sort_products(sort_type)
        
        assert is_sorted, f"Products could not be sorted by '{sort_type}'."
        
        allure.attach(driver.get_screenshot_as_png(), name=f"product_sorted_{sort_type}", attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name=f"product_sort_error_{sort_type}", attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"Test failed for sorting by '{sort_type}': {str(e)}")
