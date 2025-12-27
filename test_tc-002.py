from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_explicit_wait(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    start = time.time()

    enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_button.click()

    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))

    message = driver.find_element(By.ID, "message").text
    assert message == "It's enabled!"
    assert input_field.is_enabled()

    print(f"Time taken with explicit wait: {time.time() - start} seconds")