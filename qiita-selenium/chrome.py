import json 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MyDriver():
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.options.add_argument("--window-size=1920,1200")

    def get_pages(self, url):
        driver = webdriver.Chrome(options=self.options, executable_path=r'/usr/local/bin/chromedriver')
        driver.get(url)
        WebDriverWait(driver, timeout=3).until(lambda d: d.find_elements_by_class_name("st-Pager"))
        el = driver.find_elements_by_css_selector('div.p-tagShow_mainBottom')
        st = driver.find_elements_by_class_name("st-Pager")
        driver.quit()

        return int(st[0].text.split(" ")[-1])


driver = MyDriver()

url = "https://qiita.com/tags/nuxt.js"
numbers = driver.get_pages(url)
print(numbers)