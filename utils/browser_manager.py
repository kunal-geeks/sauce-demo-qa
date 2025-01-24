from selenium import webdriver
import json

def get_browser():
    with open('config/config.json') as f:
        config = json.load(f)

    options = webdriver.ChromeOptions()
    if config["headless"]:
        options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(config["environment"])
    return driver
