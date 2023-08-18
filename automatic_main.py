from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
import time

# Initialization of WebDriver
# これに関してはChromeDriveをインストールして規定の位置に配置
options = webdriver.chrome.options.Options()
driver = webdriver.Chrome()

# Access the Web site
driver.get('https://noahcryal.official.ec/')

driver.find_element("xpath",'//*[@id="itemList"]/li/a/div/div/div/div[2]').click()
driver.find_element("xpath",'//*[@id="mainitmIwLjQ0Nz"]/div[1]/div[2]/div[3]/form/div[1]/button').click()

time.sleep(1)
Email = driver.find_element("xpath",'//*[@id="contactEmail"]')
LastName = driver.find_element("xpath",'//*[@id="shippingAddressLastName"]')
FirstName = driver.find_element("xpath",'//*[@id="shippingAddressFirstName"]')
PostCord = driver.find_element("xpath",'//*[@id="shippingAddressZip"]')
ChooseTown= Select(driver.find_element("xpath",'//*[@id="shippingAddressPrefectureCode"]'))
City = driver.find_element("xpath",'//*[@id="shippingAddressaddress1"]')
AddressNumber = driver.find_element("xpath",'//*[@id="shippingAddressaddress2"]')
PhoneNumber = driver.find_element("xpath",'//*[@id="shippingAddressPhoneNumber"]')
driver.find_element("xpath",'//*[@id="payment-method"]/div/fieldset/div/div[4]/div/label').click()
Extra = driver.find_element("xpath",'//*[@id="remark"]')
BankPhone = driver.find_element("xpath",'//*[@id="registerPayIDPhone"]')

Email.send_keys('sawa1020@examle.com')
LastName.send_keys('澤')
FirstName.send_keys('隆由希')
PostCord.send_keys('1100022')
ChooseTown.select_by_index(4)
City.send_keys('赤坂')
AddressNumber.send_keys('123-23-222')
PhoneNumber.send_keys('09012345678')
Extra.send_keys('何もないです')
BankPhone.send_keys('09012345678')

time.sleep(8)

'''driver.find_element("xpath",'//*[@id="register-checkout-form"]/div/button').click()
time.sleep(8)'''
# close browser
driver.quit()
print('success')

"""
# login ex.
username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')

username_input.send_keys('your_username')
password_input.send_keys('your_password')
password_input.send_keys(Keys.RETURN)

# search thing ang it in a cart
search_box = driver.find_element_by_name('search')
search_box.send_keys('desired_product')
search_box.send_keys(Keys.RETURN)

# Automated product selection and cart addition
product_link = driver.find_element_by_css_selector('.product-link')
product_link.click()

add_to_cart_button = driver.find_element_by_css_selector('.add-to-cart')
add_to_cart_button.click()

# Go to cart and check out
cart_link = driver.find_element_by_css_selector('.cart-link')
cart_link.click()

checkout_button = driver.find_element_by_css_selector('.checkout-button')
checkout_button.click()

# Form entry (e.g., address and payment information)

# Order Confirmation
place_order_button = driver.find_element_by_css_selector('.place-order')
place_order_button.click()

# close browser
driver.quit()
"""