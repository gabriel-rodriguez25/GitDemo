import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe")  # seleniumManager
driver = webdriver.Firefox(service=service_obj)

driver.implicitly_wait(3)

driver.get("http://the-internet.herokuapp.com/iframe")
driver.maximize_window()

driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
