from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
import os

os.environ['WDM_SSL_VERIFY'] = '0'

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)