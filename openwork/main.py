from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np

user_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
              ]


class MyDriver():
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.options.add_argument("--window-size=1920,1200")
        self.options.add_argument(
            "--user-agent=" + user_agent[
                np.random.randint(0, len(user_agent))
            ])

    def get_pages(self, url):
        driver = webdriver.Chrome(
            options=self.options,
            executable_path=r'/usr/local/bin/chromedriver')
        # print(self.options.arguments)
        # print(driver)
        driver.get(url)
        print(driver.title)
        company_list = driver.find_element_by_class_name(
            "testCompanyList")
        company_list


driver = MyDriver()

url = "https://www.vorkers.com/company_list?field=&pref=&src_str=&sort=2"
driver.get_pages(url)
