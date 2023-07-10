import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

driver.execute_script('window.scrollBy(0,600)')

selenium_ruby_bth = driver.find_element_by_css_selector('#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3')
selenium_ruby_bth.click()

reviews_bth = driver.find_element_by_css_selector('#product-160 > div.woocommerce-tabs.wc-tabs-wrapper > ul > li.reviews_tab > a')
reviews_bth.click()

stars = driver.find_element_by_css_selector('#commentform > p.comment-form-rating > p > span > a.star-5')
stars.click()

text = driver.find_element_by_css_selector('#comment')
text.send_keys('Nice book!')

name = driver.find_element_by_id('author')
name.send_keys('Vika')

email = driver.find_element_by_id('email')
email.send_keys('vikaarfano@mail.ru')

submit = driver.find_element_by_id('submit')
submit.click()

driver.quit()