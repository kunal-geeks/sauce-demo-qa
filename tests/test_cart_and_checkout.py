import pytest
import allure
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.header_component import HeaderComponent
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

@allure.story("Cart and Checkout Tests")
def test_add_to_cart(driver, inventory_page):

    login_page = LoginPage(driver)
    cart_page = CartPage(driver)

    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("3")
    inventory_page.add_to_cart("4")
    inventory_page.go_to_cart()

    assert cart_page.is_item_present("3"), "item_3 not found in cart"
    assert cart_page.is_item_present("4"), "item_4 not found in cart"

@allure.story("Checkout Tests")
def test_checkout_process(driver, inventory_page):

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("3")
    inventory_page.add_to_cart("4")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_complete_page = CheckoutCompletePage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_one_page.fill_checkout_information("John", "Doe", "12345")
    checkout_step_one_page.click_continue()

    checkout_overview_page = CheckoutOverviewPage(driver)
    checkout_overview_page.verify_totals("$45.98", "$3.68", "$49.66")
    checkout_overview_page.click_finish()
    assert checkout_complete_page.verify_order_completion_message(), "Order completion message verification failed!"

@allure.story("Negative Tests")
def test_invalid_checkout(driver, inventory_page):

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_to_cart("5")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_one_page.fill_checkout_information("", "", "")
    checkout_step_one_page.click_continue()

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Error: First Name is required" in error_message, "Error message not displayed"
