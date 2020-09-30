from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск двух чисел и их суммирование
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    sum=int(num1)+int(num2)
    # выбор ответа из списка
    select=Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))
    # Клик по кнопке submit
    browser.find_element_by_tag_name("button").click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()