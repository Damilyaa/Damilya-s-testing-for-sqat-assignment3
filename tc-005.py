import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)
driver.save_screenshot("before_dropdown.png")

dropdown_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "dropdown")))

ActionChains(driver).move_to_element(dropdown_element).perform()

dropdown_element.click()

dropdown_option = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//option[text()='Option 1']")))
dropdown_option.click()

time.sleep(2)

driver.save_screenshot("after_dropdown.png")

driver.quit()