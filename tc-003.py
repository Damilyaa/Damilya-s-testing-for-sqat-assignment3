import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)
driver.save_screenshot("before_drag_and_drop.png")

drag = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "column-a")))
drop = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "column-b")))
ActionChains(driver).drag_and_drop(drag, drop).perform()

time.sleep(2)

driver.save_screenshot("after_drag_and_drop.png")

driver.quit()