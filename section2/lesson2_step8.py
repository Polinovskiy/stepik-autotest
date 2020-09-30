from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # заполенение формы
    browser.find_element_by_name("firstname").send_keys("Dima")
    browser.find_element_by_name("lastname").send_keys("Petrov")
    browser.find_element_by_name("email").send_keys("fewf@fe.ru")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    print(current_dir)
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 
    print(file_path)
    browser.find_element_by_id("file").send_keys(file_path)

    # Отправляем заполненную форму
    browser.find_element_by_tag_name("button").click()

   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()