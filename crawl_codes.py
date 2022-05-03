bojid = "yourid"
password = "yourpassword"

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import paperclip as pc

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

driver.get("https://www.acmicpc.net/user/"+bojid)

arr = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div/a")
time.sleep(3)

nums = []
for dt in arr:
	nums.append(dt.get_attribute('innerText'))

for num in nums:
	driver.get('https://www.acmicpc.net/status?problem_id='+num+'&user_id='+bojid+'&language_id=-1&result_id=4&from_mine=1')
	driver.implicitly_wait(3)
	accodes = driver.find_elements_by_xpath('//*[@id="status-table"]/tbody/tr')
	langurl,codeurl = accodes[-1].find_elements_by_xpath('td[7]/a')
	lang = langurl.get_attribute('innerText')

	driver.get(codeurl.get_attribute('href'))

	code = ""
	cursor = driver.find_element_by_xpath('//*[@id="source"]')

	file = open('codes/'+num+'.'+lang, "w")
	file.write(cursor.get_attribute('value'))
	file.close()
