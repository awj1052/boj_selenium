from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

import SolvedData, FileService

import AccountData

def init(driver):
    driver.get('https://www.acmicpc.net/login?next=%2F')
    driver.find_element(By.NAME, 'login_user_id').send_keys(AccountData.ID)
    element = driver.find_element(By.NAME, 'login_password')
    element.send_keys(AccountData.PW)
    driver.find_element(By.NAME, 'auto_login').click()
    element.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/div/div[2]/ul/li[7]/a').click() # 그룹
    driver.find_element(By.XPATH, '//*[@id="ranklist"]/tbody/tr/td[1]/a').click() # 첫 번째 그룹
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/ul/li[3]/a').click() # 채점 현황

def get_recent_solved_problem(driver, last_solution):
    first_solution_number = 0
    solved_data = []
    while True:
        table = driver.find_element(By.ID, 'status-table')
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        rows = tbody.find_elements(By.TAG_NAME, 'tr')
        for index, value in enumerate(rows):
            body=value.find_elements(By.TAG_NAME, 'td')
            solution_number = body[0].text
            user_name = body[1].find_element(By.TAG_NAME, 'a').text
            problem_number = body[2].find_element(By.CLASS_NAME, 'problem_title').text
            result = body[3].find_element(By.CLASS_NAME, 'result-text').text

            if first_solution_number == 0:
                first_solution_number = int(solution_number)
            
            if int(solution_number) <= last_solution:
                FileService.update_last_solution(first_solution_number)
                return solved_data
            
            solved_data.append(SolvedData.SolvedData(solution_number, user_name, problem_number, result))
        driver.find_element(By.ID, 'next_page').click()
        time.sleep(1)