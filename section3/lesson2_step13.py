import unittest
from selenium import webdriver
import time

def reg(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector("div.first_block input.first").send_keys("Дима")
    browser.find_element_by_css_selector("div.first_block input.second").send_keys("Петров")
    browser.find_element_by_css_selector("div.first_block input.third").send_keys("jfiejw@fjeij.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text

class Registration(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual("Congratulations! You have successfully registered!", reg("http://suninjuly.github.io/registration1.html"))
    def test_reg2(self):
        self.assertEqual("Congratulations! You have successfully registered!", reg("http://suninjuly.github.io/registration2.html"))

if __name__ == "__main__":
    unittest.main()