from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os

os.environ['WDM_SSL_VERIFY'] = '0'

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
