import os
from datetime import datetime

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
    os.makedirs("screenshots", exist_ok=True)
    driver.save_screenshot(screenshot_path)
    return screenshot_path
