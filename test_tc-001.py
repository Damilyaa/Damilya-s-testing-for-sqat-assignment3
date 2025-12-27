import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_implicit_wait(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    driver.implicitly_wait(5)  

    start = time.time()
    enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_button.click()

    message = driver.find_element(By.ID, "message").text
    input_field = driver.find_element(By.XPATH, "//input[@type='text']")

    print(f"Time taken with implicit wait: {time.time() - start} seconds")
    assert message == "It's enabled!"
    assert input_field.is_enabled()