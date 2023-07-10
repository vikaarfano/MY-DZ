from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

my = driver.find_element_by_css_selector('#menu-item-50 > a')
my.click()

email = driver.find_element_by_css_selector('#username')
email.send_keys('vikaarfano@mail.ru')

password = driver.find_element_by_css_selector('#password')
password.send_keys('Macroarfano111')

shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()

html = driver.find_element_by_css_selector('#woocommerce_product_categories-2 > ul > li.cat-item.cat-item-19 > a')
html.click()

items_count = driver.find_elements_by_class_name('attachment-shop_catalog.size-shop_catalog.wp-post-image')
if len(items_count) == 3: # после 1-го урока можем теперь создать небольшую конструкцию для проверки кол-ва товаров
    print("На странице 3 товара") # len здесь посчитает количество элементов, найденных при помощи find_elements
else:
    print("Ошибка. Количество товаров: " + str(len(items_count)))
