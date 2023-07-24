from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#set up the Webdriver and navigate  to website url
driver = webdriver.Chrome()
url = driver.get("http://demostore.supersqa.com/")
# locate to one of the item and click on it
item = driver.find_element(By.CSS_SELECTOR, '#main > ul > li.product.type-product.post-16.status-publish.last.instock.product_cat-accessories.has-post-thumbnail.sale.shipping-taxable.purchasable.product-type-simple > a.woocommerce-LoopProduct-link.woocommerce-loop-product__link > img')
item.click()
#locate to "add to cart" button and click on it
add_to_cart_btn = driver.find_element(By.CSS_SELECTOR, "#product-16 > div.summary.entry-summary > form > button")
add_to_cart_btn.click()

# locate to cart and click on it
cart = driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a')
cart.click()

#locate to cuopon code and enter invalid coupon
coupon_input = driver.find_element(By.ID, "coupon_code")
coupon_input.send_keys("summer2023")
coupon_input.send_keys(Keys.ENTER)

#locate to error message and wait until it is visible on the page
err_mess_locator = (By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul/li')
error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(err_mess_locator))
displayed_message = error_message.text
expected_message = 'Coupon "summer2023" does not exist!'

#verify the error message
if displayed_message != expected_message:
    error_msg = f"Error: The displayed coupon message does not match the expected message.\n"\
                    f"Expected:'{expected_message}'\nActual: '\'{displayed_message}'"
    raise Exception(error_msg)
else:
    print("Coupon code validation successful: Invalid coupon code.")

    print("Test Passed Successfully.")

#close the browser
driver.quit()