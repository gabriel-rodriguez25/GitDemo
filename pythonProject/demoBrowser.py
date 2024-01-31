from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#Chrome driver - Chrome browser
# -- CHROME
# service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe") #seleniumManager
# driver = webdriver.Chrome(service=service_obj)

# -- FIREFOX
service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe") #seleniumManager
driver = webdriver.Edge(service=service_obj)


driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()



# service_obj = Service("/Users/Gabriel.Rodriguez/Documents/chrome-win64/chrome.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com")
# driver.close()