from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--user-data-dir=/Users/mattheweng/Library/Application Support/Google/Chrome/Default")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mattheweng/bin/chromedriver')
print(0)
driver.get("https://iapps.courts.state.ny.us/webcivilLocal/LCSearch?param=I")
print(1)
driver.implicitly_wait(10)
WebDriverWait(driver, 100).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='https://www.google.com/recaptcha/api2/anchor?']")))
print(1.5)
driver.implicitly_wait(10)
WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.recaptcha-checkbox.goog-inline-block.recaptcha-checkbox-unchecked.rc-anchor-checkbox"))).click()
print(1.7)
driver.switch_to_default_content()
# WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
print(2)
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
