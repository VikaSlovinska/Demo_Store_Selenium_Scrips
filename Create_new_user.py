from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

url = driver.get("http://demostore.supersqa.com/my-account/")

email_field = driver.find_element(By.ID, 'reg_email')
email_field.click()
register_email = email_field.send_keys("N.aaamash@gmail.com")

password_field = driver.find_element(By.ID, 'reg_password')
password_field.click()

register_password = password_field.send_keys('Enriched2021')

register_btn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column2.col-2 > form > p:nth-child(4) > button')
register_btn.click()
