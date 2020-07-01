import time

from selenium import webdriver
from secrets import username, password


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

        tinderWindow = self.driver.window_handles[0]
        # switch to login popup
        self.driver.switch_to_window(self.driver.window_handles[1])
        # fill email and pass fields
        emailIn = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input"
        )
        emailIn.send_keys(username)
        passIn = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input"
        )
        passIn.send_keys(password)
        loginBtn = self.driver.find_element_by_xpath(
            "/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input"
        )
        loginBtn.click()
        time.sleep(3)
        self.driver.switch_to_window(tinderWindow)
        permitBtn = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[1]"
        )
        permitBtn.click()
        notifBtn = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[2]"
        )
        notifBtn.click()

    def like(self):
        likeBtn = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button"
        )
        likeBtn.click()

    def dislike(self):
        dislikeBtn = self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button"
        )
        dislikeBtn.click()

    def autoLike(self):
        while True:
            time.sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    closePopup()
                except Exception:
                    self.closeMatch()

    def closePopup(self):
        popupBtn = self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[2]/button[2]"
        )
        popupBtn.click()

    def closeMatch(self):



bot = TinderBot()
bot.login()
# bot.autoLike()
