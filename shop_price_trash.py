import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')


shop = driver.find_element_by_css_selector('#menu-item-40 > a')
shop.click()

add = driver.find_element_by_css_selector('#content > ul > li.post-182.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.last.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.button.product_type_simple.add_to_cart_button.ajax_add_to_cart')
add.click()

time.sleep(5)

col = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[1]')
col_text = col.text
assert "1" in col_text

price = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[2]')
price_text = price.text
assert "180.00" in price_text

trash = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a')
trash.click()

price180 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span')))

total = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span")))


