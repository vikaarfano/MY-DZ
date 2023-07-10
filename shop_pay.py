import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()

driver.execute_script('window.scrollBy(0,300)')

html_add = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
html_add.click()
time.sleep(3)

trash = driver.find_element_by_css_selector('#wpmenucartli > a > span.amount')
trash.click()

bth = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#page-34 > div > div.woocommerce > div > div > div > a')))
bth.click()

name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#billing_first_name')))
name.send_keys('Vika')

last = driver.find_element_by_id('billing_last_name')
last.send_keys('Arfano')

email = driver.find_element_by_id('billing_email')
email.send_keys('vikaarfano@mail.ru')

phone = driver.find_element_by_id('billing_phone')
phone.send_keys('89252820555')

coun = driver.find_element_by_id('s2id_billing_country')
coun.click()

russia = driver.find_element_by_id('s2id_autogen1_search')
russia.send_keys('Russia')

rus = driver.find_element_by_class_name('select2-results-dept-0.select2-result.select2-result-selectable')
rus.click()

adress = driver.find_element_by_id('billing_address_1')
adress.send_keys('Москва, фестивальная 73к3, кв 98')

town = driver.find_element_by_id('billing_city')
town.send_keys('Москва')

co = driver.find_element_by_id('billing_state')
co.send_keys('Москва')

zip = driver.find_element_by_id('billing_postcode')
zip.send_keys('1256854')

driver.execute_script('window.scrollBy(0,600)')
time.sleep(5)

check = driver.find_element_by_id('payment_method_cheque')
check.click()

place = driver.find_element_by_id('place_order')
place.click()
time.sleep(3)

text1 = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35 > div > div.woocommerce > table > tfoot > tr:nth-child(3) > td'), 'Check Payments'))

text = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35 > div > div.woocommerce > p.woocommerce-thankyou-order-received'), 'Thank you. Your order has been received.'))

driver.quit()


