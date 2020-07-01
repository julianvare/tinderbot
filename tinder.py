import time
import sys

from selenium import webdriver


class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://tinder.com")
        time.sleep(3)
        fbBtn = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button"
        )
        fbBtn.click()


print(sys.version)
bot = TinderBot()
bot.login()
