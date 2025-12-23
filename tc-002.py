from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")
enable_button.click()

start = time.time()

wait = WebDriverWait(driver, 10)
input_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='text']")))

message = driver.find_element(By.ID, "message").text

print(f"Message: '{message}'")
print(f"Input enabled: {input_field.is_enabled()}")
print(f"Took: {time.time() - start:.2f}s")

driver.quit()