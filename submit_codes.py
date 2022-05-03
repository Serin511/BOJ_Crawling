bojid = "bojid"
yourpassword = "yourpassword"

import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import clipboard

LANG = {"C++20":95, "C++11":49, "C++17":84, "C++14":88, "C++20 (Clang)":96, "Python 3":28, "PyPy3":73, "Text":58}
#딴건 알아서~

path = 'codes/'
file_list = os.listdir(path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('ignore-certificate-errors')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-suage')
driver = webdriver.Chrome("./chromedriver", options=chrome_options)

driver.get("https://www.acmicpc.net/login")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/input').send_keys(bojid)
driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/input').send_keys(yourpassword)
time.sleep(10)

for filename in file_list:
	file = open(path+filename, "r")
	num,lang = filename.split('.')
	driver.get("https://www.acmicpc.net/submit/"+num)
	time.sleep(3)

	code = str(file.read())	
	clipboard.copy(code)
	element = driver.switch_to.active_element
	element.send_keys(Keys.CONTROL, 'v')

	langbox = driver.find_element_by_xpath('//*[@id="language_chosen"]/div/div/input')
	langbox.send_keys(lang+Keys.ENTER)

	driver.find_element_by_xpath('//*[@id="submit_button"]').click()

	file.close()
	time.sleep(20)
