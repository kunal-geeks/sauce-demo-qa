import pytest
import allure
import json
from pages.login_page import LoginPage

# Load test data from login_test_data.json
def load_test_data():
    with open("data/login_test_data.json", "r") as file:
        return json.load(file)

test_data = load_test_data()

@allure.feature("Login Tests")
@allure.story("Valid Logins")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("user", test_data["valid_logins"])
def test_valid_login(driver, user):
    with allure.step(f"Testing valid login for {user['username']}"):
        login_page = LoginPage(driver)
        login_page.login(user["username"], user["password"])
        assert "inventory.html" in driver.current_url, f"Login failed for {user['username']}"
        allure.attach(driver.get_screenshot_as_png(), name=f"valid_login_{user['username']}", attachment_type=allure.attachment_type.PNG)

@allure.feature("Login Tests")
@allure.story("Invalid Logins")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize("user", test_data["invalid_logins"])
def test_invalid_login(driver, user):
    with allure.step(f"Testing invalid login for {user['username']}"):
        login_page = LoginPage(driver)
        login_page.login(user["username"], user["password"])
        assert "inventory.html" not in driver.current_url, f"Login succeeded for {user['username']} when it should have failed"
        allure.attach(driver.get_screenshot_as_png(), name=f"invalid_login_{user['username']}", attachment_type=allure.attachment_type.PNG)

@allure.feature("Login Tests")
@allure.story("Edge Case Logins")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("user", test_data["edge_case_logins"])
def test_edge_case_login(driver, user):
    with allure.step(f"Testing edge case login for {user['username']}"):
        login_page = LoginPage(driver)
        login_page.login(user["username"], user["password"])
        assert "inventory.html" not in driver.current_url, f"Edge case login succeeded for {user['username']} when it should have failed"
        allure.attach(driver.get_screenshot_as_png(), name=f"edge_case_login_{user['username']}", attachment_type=allure.attachment_type.PNG)
