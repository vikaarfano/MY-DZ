from selenium import webdriver
from selenium.webdriver.support.select import Select
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

defolt = driver.find_element_by_class_name('orderby')
defolt_yes = defolt.get_attribute('menu_order') # создали переменную, в которую поместим значение атрибута
print('value of defolt:', defolt_yes) # выводим в консоль значение атрибута
if defolt_yes is None: # проверяем, если значение атрибута НЕ пустое, значит чекбокс отмечен
    print('Defolt=Defolt')
else:
    print('Defolt not Defolt')

select = Select(defolt)
select.select_by_value ('price-desc')

high = driver.find_element_by_class_name('orderby')
high_yes = high.get_attribute('menu_order') # создали переменную, в которую поместим значение атрибута
print('value of high:', high_yes) # выводим в консоль значение атрибута
if high_yes is None: # проверяем, если значение атрибута НЕ пустое, значит чекбокс отмечен
    print('High=High')
else:
    print('High not High')