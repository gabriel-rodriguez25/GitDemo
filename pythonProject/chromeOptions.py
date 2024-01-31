from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")  # The window will not be displayed
chrome_options.add_argument("--ignore-certificate-errors")

# service_obj = Service("C:/Users/gabriel.rodriguez/Documents/chromedriver.exe",)  # seleniumManager
service = webdriver.ChromeService(executable_path="C:\\Users\\gabriel.rodriguez\\Documents\\chromedriver.exe",
                                  options=chrome_options)

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
