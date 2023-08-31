import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os

os.environ['WDM_SSL_VERIFY'] = '0'

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://www.wikipedia.org/")
url = driver.current_url
print("URL страницы:", url)
time.sleep(3)
current_title = driver.title
print("Текущий заголовок:", current_title)

assert url == "https://www.wikipedia.org/", f"Ошибка в URL, открыта страница {url}"
assert current_title == "Wikipedia", "Некорректный заголовок страницы"

print(driver.page_source)