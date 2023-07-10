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

lod = driver.find_element_by_css_selector('#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button')
lod.click()

logout= driver.find_element_by_css_selector('#page-36 > div > div.woocommerce > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a')
logout_text = logout.text
assert 'Logout' in logout_text

driver.quit()