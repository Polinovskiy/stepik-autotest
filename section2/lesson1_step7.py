from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск x и вычисление f(x)
    x = browser.find_element_by_id("treasure").get_attribute("valuex")
    y=calc(x)
    # ввод результата f(x) в поле формы
    browser.find_element_by_id("answer").send_keys(y)
    # выставлнение чекбокса Я - робот
    browser.find_element_by_id("robotCheckbox").click()
    # Установка радиокнопки робот рулит
    browser.find_element_by_id("robotsRule").click()
    # Отправляем заполненную форму
    browser.find_element_by_tag_name("button").click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()