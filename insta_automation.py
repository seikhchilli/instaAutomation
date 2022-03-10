import os
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:\Users\saura\Desktop"
driver = webdriver.Chrome()

driver.get("https://www.instagram.com/?hl=en")

driver.implicitly_wait(5)

try:
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
except:
    print("no element found with this name")

username.send_keys("your_insta_username")   #replace it with your insta username
password.send_keys("your_insta_password")   #replace it with your insta password
password.send_keys(Keys.RETURN)

try:
    not_now = driver.find_element_by_class_name("cmbtv")
except:
    print("no element with this class name")

not_now.click()

try:
    not_now2 = driver.find_element_by_class_name("HoLwm")
except:
    print("no element with this class name")

not_now2.click()

see_all = driver.find_element_by_link_text("See All")
see_all.click()

for i in range(1, 30):
    follow_link = driver.find_element_by_xpath(f"html/body/div/section/main/div/div[2]/div/div/div[{i}]/div[3]")
    follow_link.click()