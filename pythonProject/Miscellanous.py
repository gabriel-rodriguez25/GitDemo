import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("headless")  # so the browser window is not opened

service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe")  # seleniumManager
driver = webdriver.Chrome(service=service_obj, options=chromeOptions)  # the <,options=chromeOptions> was added so the browser window is not opened

chromeOptions.add_argument("--ignore-certificate-errors") # bypass the certificate errors screens

driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(3)
driver.get_screenshot_as_file("screen.png")
