from selenium import webdriver

driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

my = driver.find_element_by_css_selector('#menu-item-50 > a')
my.click()

email = driver.find_element_by_css_selector('#menu-item-50 > a')
email.send_keys('vikaarfano@mail.ru')

password = driver.find_element_by_css_selector('#reg_password')
password.send_keys('Macroarfano111')

registr = driver.find_element_by_css_selector('#customer_login > div.u-column2.col-2 > form > p.woocomerce-FormRow.form-row > input.woocommerce-Button.button')
registr.click()

driver.quit()