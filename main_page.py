import os

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fake = Faker()
login = fake.user_name()
password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

driver_path = os.path.join(os.getcwd(), 'chromedriver.exe')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
link = "https://store.steampowered.com/"
driver.get(link)
driver.maximize_window()

login_button = driver.find_element(By.XPATH, "//a[contains(@class,'global_action_link')]")
login_button.click()

account_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='_3BkiHun-mminuTO-Y-zXke']//input[@type='text']")))
account_name.send_keys(login)

account_pass = driver.find_element(By.XPATH, "//div[@class='_3BkiHun-mminuTO-Y-zXke']//input[@type='password']")
account_pass.send_keys(password)

sign_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_button.click()

message_error = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//div[@class='_1W_6HXiG4JJ0By1qN_0fGZ']"),
                                     "Please check your password and account name and try again."))

alert_message_element = driver.find_element(By.XPATH, "//div[@class='_1W_6HXiG4JJ0By1qN_0fGZ']")
error_text = alert_message_element.text
print(f"Error text: {error_text}")
