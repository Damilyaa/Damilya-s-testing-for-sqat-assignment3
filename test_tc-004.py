import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_hover(driver):
    driver.get("https://the-internet.herokuapp.com/hovers")
    time.sleep(2)
    driver.save_screenshot("before_hover.png")

    hover_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "figure")))

    ActionChains(driver).move_to_element(hover_element).perform()

    time.sleep(2)

    driver.save_screenshot("after_hover.png")