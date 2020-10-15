import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def timeIs():
    return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"]) 
def test_guest_should_see_login_link(browser, id):
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)
    textarea= WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH, "//textarea"))).send_keys(timeIs())
    browser.find_element_by_css_selector(".submit-submission").click()
    label = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//pre[@class='smart-hints__hint']")))
    assert label.text == "Correct!", f"Expected text is 'Correct!', but we have {label.text}"
    