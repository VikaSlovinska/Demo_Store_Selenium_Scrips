from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = driver.get("http://demostore.supersqa.com/my-account/")

username = driver.find_element(By.ID, 'username')
username.send_keys("N.aaamash@gmail.com")

password = driver.find_element(By.ID, 'password')
password.send_keys('Enriched2021')

login_btn = driver.find_element(By.CSS_SELECTOR, '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button')
login_btn.click()

notice_locator = (By.XPATH, '//*[@id="post-9"]/div/div/div/p[1]')
greeting_text = WebDriverWait(driver, 25).until(EC.visibility_of_element_located(notice_locator))

expected_username = "n.aaamash"
expected_greeting = f"Hello {expected_username} (not {expected_username}? Log out)"

assert expected_greeting == greeting_text.text, f"Greeting failed. Expected_greeting = '{expected_greeting}'. Actual greeting : '{greeting_text.text}"
print("Greeting text :", greeting_text.text)

