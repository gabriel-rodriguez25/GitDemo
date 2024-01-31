import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []

service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe")  # seleniumManager
driver = webdriver.Chrome(service=service_obj)

driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()

# driver.find_element(By.CSS_SELECTOR,".sort-descending").click()
# #time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,".sort-ascending").click()

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedveggieList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this veggieList => newSortedList
browserSortedVeggies.sort()

# BrowserSortedveggieList == newSortedList
assert browserSortedVeggies == originalBrowserSortedList

time.sleep(3)
