import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown(driver):
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )

    select = Select(dropdown_element)

    select.select_by_visible_text("Option 1")

    selected = select.first_selected_option.text
    assert selected == "Option 1"
