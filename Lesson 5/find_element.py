import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os

os.environ['WDM_SSL_VERIFY'] = '0'

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.freeconferencecall.com/global/by/login")
print(driver.find_element("id", "loginformsubmit"))

# Способы поиска, эквивалентные By.***:
# ➖ ID = "id"
# ➖ XPATH = "xpath"
# ➖ NAME = "name"
# ➖ CLASS_NAME = "class name"
# ➖ CSS_SELECTOR = "css selector"
