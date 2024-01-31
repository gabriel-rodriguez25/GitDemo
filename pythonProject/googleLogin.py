import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe") #seleniumManager
driver = webdriver.Firefox(service=service_obj)

driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"gb_Id").click()
header=driver.find_element(By.CLASS_NAME,"oO8pQe").text
print(header)

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("jogaevil25@gmail.com")
driver.find_element(By.ID,"identifierNext").click()

time.sleep(7)

driver.close()