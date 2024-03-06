from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from AccountData import *

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)

# 구글 뉴스 페이지 열기
driver.get('https://www.acmicpc.net/login?next=%2F')
driver.find_element(By.NAME, 'login_user_id').send_keys(ID)
element = driver.find_element(By.NAME, 'login_password')
element.send_keys(PW)
element.send_keys(Keys.ENTER)
time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[7]/a').click() # 그룹
driver.find_element(By.XPATH, '//*[@id="ranklist"]/tbody/tr/td[1]/a').click() # 첫 번째 그룹
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[3]/a').click() # 채점 현황