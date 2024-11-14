from selenium.webdriver.chrome.options import Options

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()
login = fake.user_name()
password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

LOGIN_BUTTON_LOCATOR = "//a[contains(@class,'global_action_link')]"
ACCOUNT_NAME_LOCATOR = "//div[contains(@class,'_3BkiHun-mminuTO-Y-zXke')]//input[@type='text']"
ACCOUNT_PASS_LOCATOR = "//div[contains(@class,'_3BkiHun-mminuTO-Y-zXke')]//input[@type='password']"
SIGN_BUTTON_LOCATOR = "//button[@type='submit']"
MESSAGE_ERROR_LOCATOR = "//div[contains(@class,'_1W_6HXiG4JJ0By1qN_0fGZ')]"
MESSAGE_ERROR = "Pleas check your password and account name and try again."
TIMEOUT = 10

options = Options()
driver = webdriver.Chrome(options=options)
LINK = "https://store.steampowered.com/"
driver.get(LINK)
driver.delete_all_cookies()

login_button = WebDriverWait(driver, TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON_LOCATOR)))
login_button.click()

account_name = WebDriverWait(driver, TIMEOUT).until(
    EC.visibility_of_element_located((By.XPATH, ACCOUNT_NAME_LOCATOR)))
account_name.send_keys(login)

account_pass = WebDriverWait(driver, TIMEOUT).until(
    EC.visibility_of_element_located((By.XPATH, ACCOUNT_PASS_LOCATOR)))
account_pass.send_keys(password)

sign_button = WebDriverWait(driver, TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, SIGN_BUTTON_LOCATOR)))
sign_button.click()

sign_button = WebDriverWait(driver, TIMEOUT).until(
    EC.element_to_be_clickable((By.XPATH, SIGN_BUTTON_LOCATOR)))

message_error = WebDriverWait(driver, TIMEOUT).until(
    EC.visibility_of_element_located((By.XPATH, MESSAGE_ERROR_LOCATOR)))

assert MESSAGE_ERROR in message_error.text, f"""Expected :{MESSAGE_ERROR}
                Actual result:{message_error.text}"""
