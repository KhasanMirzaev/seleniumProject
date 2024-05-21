from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Initialize the WebDriver
driver = webdriver.Chrome()

driver.get('https://www.saucedemo.com')

driver.maximize_window()

sleep(1)

#username kiritish
driver.find_element(By.CSS_SELECTOR, '*[data-test="username"]').send_keys('standard_user')
sleep(1)

#parol kiritish
driver.find_element(By.CSS_SELECTOR, '*[data-test="password"]').send_keys('secret_sauce')
sleep(1)

#login buttonga bosing
driver.find_element(By.CSS_SELECTOR, '*[data-test="login-button"]').click()
sleep(1)

#product qo'shish
driver.find_element(By.CSS_SELECTOR, '*[data-test="add-to-cart-sauce-labs-backpack"]').click()
sleep(1)

#product qo'shish
driver.find_element(By.CSS_SELECTOR, '*[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
sleep(1)

#product qo'shish
driver.find_element(By.CSS_SELECTOR, '*[data-test="add-to-cart-sauce-labs-onesie"]').click()
sleep(1)

#product qo'shish
driver.find_element(By.CSS_SELECTOR, '*[data-test="add-to-cart-sauce-labs-bike-light"]').click()
sleep(1)

#product qo'shish
driver.find_element(By.CSS_SELECTOR, '*[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
sleep(1)

#product qo'shish
driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
sleep(1)

#cart buttonga bosish
driver.find_element(By.CSS_SELECTOR, '*[data-test="shopping-cart-link"]').click()
sleep(1)

#checkout buttonga bosish
driver.find_element(By.CSS_SELECTOR, '*[data-test="checkout"]').click()
sleep(1)

#ism kiritish
driver.find_element(By.CSS_SELECTOR, '[data-test="firstName"] ').send_keys('falonchi')
sleep(1)

#familiya kiritish
driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"] ').send_keys('tugunchiyev')
sleep(1)

#ZIP kiritish
driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"] ').send_keys('123456')
sleep(1)

#continue buttonga bosish
driver.find_element(By.CSS_SELECTOR, '[data-test="continue"] ').click()
sleep(1)

#finish buttonga bosish
driver.find_element(By.CSS_SELECTOR, '[data-test="finish"] ').click()
sleep(1)

#home page ga qaytish
driver.find_element(By.CSS_SELECTOR, '[data-test="back-to-products"] ').click()
sleep(2)

#brauzerni yopish
driver.quit()