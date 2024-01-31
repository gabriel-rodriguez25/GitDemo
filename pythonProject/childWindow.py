import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe")  # seleniumManager
driver = webdriver.Firefox(service=service_obj)

driver.implicitly_wait(3)

driver.get("http://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()
windowOpened = driver.window_handles

driver.switch_to.window(windowOpened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close

#Switch back to parent window again
driver.switch_to.window(windowOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text

driver.close()
