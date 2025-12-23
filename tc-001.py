import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

time.sleep(2)

enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
enable_button.click()

start = time.time()

time.sleep(5)

message = driver.find_element(By.ID, "message").text
input_field = driver.find_element(By.XPATH, "//input[@type='text']")

print(f"Message: '{message}'")
print(f"Input enabled: {input_field.is_enabled()}")
print(f"Took: {time.time() - start:.2f}s")

driver.quit()