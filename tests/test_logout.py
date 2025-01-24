import allure
from pages.header_component import HeaderComponent
from pages.login_page import LoginPage
from utils.wait import wait_for_element_to_be_visible
@allure.feature("Logout Tests")
@allure.story("Valid Logout")
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_logout(driver):
    with allure.step("Testing valid logout"):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        header_component = HeaderComponent(driver)
        
        # Perform the logout action
        header_component.logout()

        # Assert that the user is logged out by checking the presence of the login button
        try:
            assert login_page.is_login_button_displayed(), "Login button is not visible after logout."
            allure.attach(driver.get_screenshot_as_png(), name="valid_logout", attachment_type=allure.attachment_type.PNG)
            allure.step("Logout successful. Login button is visible.")
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), name="logout_error", attachment_type=allure.attachment_type.PNG)
            allure.step(f"Error during logout test: {e}")
            raise

@allure.feature("Logout Tests")
@allure.story("Edge Case: Already Logged Out")
@allure.severity(allure.severity_level.NORMAL)
def test_logout_already_logged_out(driver):
    with allure.step("Testing logout when user is already logged out"):
        header_component = HeaderComponent(driver)

        # Check if already logged out
        if header_component.is_logged_out():
            allure.step("User is already logged out. No action performed.")
        else:
            # Perform logout if not already logged out
            header_component.logout()
            assert header_component.is_logged_out(), "Logout failed when trying to log out."
            allure.attach(driver.get_screenshot_as_png(), name="logout_already_logged_out", attachment_type=allure.attachment_type.PNG)
