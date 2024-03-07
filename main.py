from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import AccountData

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.acmicpc.net/login?next=%2F')
driver.find_element(By.NAME, 'login_user_id').send_keys(AccountData.ID)
element = driver.find_element(By.NAME, 'login_password')
element.send_keys(AccountData.PW)
element.send_keys(Keys.ENTER)
time.sleep(1)
button = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[7]/a').click() # 그룹
driver.find_element(By.XPATH, '//*[@id="ranklist"]/tbody/tr/td[1]/a').click() # 첫 번째 그룹
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[3]/a').click() # 채점 현황

table = driver.find_element(By.ID, 'status-table')
tbody = table.find_element(By.TAG_NAME, 'tbody')
rows = tbody.find_elements(By.TAG_NAME, 'tr')
cnt = 0
for index, value in enumerate(rows):
    cnt += 1
    body=value.find_elements(By.TAG_NAME, 'td')
    solution_number = body[0].text
    user_name = body[1].find_element(By.TAG_NAME, 'a').text
    problem_number = body[2].find_element(By.CLASS_NAME, 'problem_title').text
    print(solution_number, user_name, problem_number)
print("DATA SIZE", cnt)

driver.close()
