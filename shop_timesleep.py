import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
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

driver.execute_script("window.scrollBy(0,300)")

add = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
add. click()
time.sleep(3)

add2 = driver.find_element_by_css_selector('#content > ul > li.post-180.product.type-product.status-publish.product_cat-javascript.product_tag-javascript.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
add2.click()

trash = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a')
trash.click()
time.sleep(3)

delete = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-remove > a')
delete.click()
time.sleep(10)

undo = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > div.woocommerce-message > a')
undo.click()
time.sleep(10)

clear = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
clear.clear()
clear.send_keys(3)

upd = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > input.button')
upd.click()
time.sleep(5)

t3 = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input')
t3_text = t3.get_attribute('value')
assert "3" in t3_text

time.sleep(3)
apply = driver.find_element_by_css_selector('#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button')
apply.click()

wind = driver.find_element_by_class_name('woocommerce-error')
wind_text = wind.text
assert 'Please enter a coupon code.' in wind_text

driver.quit()
