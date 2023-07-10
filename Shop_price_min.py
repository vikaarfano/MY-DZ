from selenium import webdriver
from selenium.webdriver.support.select import Select
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

quick = driver.find_element_by_css_selector('#content > ul > li.post-169.product.type-product.status-publish.product_cat-android.product_tag-android.has-post-title.no-post-date.has-post-category.has-post-tag.has-post-comment.has-post-author.first.instock.sale.downloadable.taxable.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link > h3')
quick.click()

six = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > del > span')
six_text = six.text
assert "600" in six_text

four = driver.find_element_by_css_selector('#product-169 > div.summary.entry-summary > div:nth-child(2) > p > ins > span')
four_text = four.text
assert "450" in four_text

img = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'attachment-shop_single.size-shop_single.wp-post-image')))
img.click()

close = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'pp_close')))
close.click()

driver.quit()
