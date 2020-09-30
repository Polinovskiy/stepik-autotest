from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")

    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "verify"))
    )
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text
    

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()