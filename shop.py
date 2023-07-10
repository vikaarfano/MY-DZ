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

html = driver.find_element_by_css_selector('#content > ul > li.post-181.product.type-product.status-publish.product_cat-html.product_tag-html.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.instock.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3')
html.click()

h1 = driver.find_element_by_css_selector('#product-181 > div.summary.entry-summary > h1')
h1_text = h1.text
assert 'HTML5 Forms' in h1_text

driver.quit()