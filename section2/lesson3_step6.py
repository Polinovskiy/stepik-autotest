from selenium import webdriver
import time
import os
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # клик по кнопке и подтверждение алерта
    browser.find_element_by_tag_name("button").click()
    browser.switch_to.window(browser.window_handles[-1])
    print(browser.window_handles[-1].name)
    
    # поиск x и вычисление f(x)
    x = browser.find_element_by_id("input_value").text
    y=calc(x)
    # ввод результата f(x) в поле формы
    browser.find_element_by_id("answer").send_keys(y)
    # Отправляем заполненную форму
    browser.find_element_by_tag_name("button").click()
    

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()