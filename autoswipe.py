from selenium import webdriver
from time import sleep


class TinderBot():

    phonenumber = ''

    def __init__(self, phonenumber):
        self.driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
        self.phonenumber = phonenumber
    def login(self):
        self.driver.get('https://www.tinder.com')
        sleep(5)
        try:
            login_with_mobile_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/button')
        except Exception:
            login_with_mobile_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button')
        except:
            login_with_mobile_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        login_with_mobile_btn.click()
        sleep(1)
        input_number = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        input_number.send_keys('value', self.phonenumber)
        continue_btn= self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        continue_btn.click()
    
    def confirm_login(self):
        allow_location_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_location_btn.click()
        allow_notifications_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_notifications_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('')
        like_btn.click()

    def dislike(self):
        like_btn = self.driver.find_element_by_xpath('')
        like_btn.click()


class BumbleBot():

    phonenumber = ''
    password = ''

    def __init__(self, phonenumber, password):
        self.driver = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver')
        self.phonenumber = phonenumber
        self.password = password

    def login(self):
        self.driver.get('https://bumble.com/')
        login_btn = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        login_btn.click()
        sleep(1)
        login_with_mobile_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[3]/div')
        login_with_mobile_btn.click()
        input_number = self.driver.find_element_by_xpath('//*[@id="phone"]')
        input_number.send_keys('value', self.phonenumber)
        continue_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[4]/button')
        continue_btn.click()
        sleep(1)
        input_password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        input_password.send_keys(self.password)
        sign_in_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[2]/button')
        sign_in_btn.click()
    
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
        like_btn.click()

    def dislike(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div')
        like_btn.click()

    def autolike(self, sleep_time):
        while True:
            sleep(sleep_time)
            bot.like()
