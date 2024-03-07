from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import FileService, WebService

if __name__ == "__main__":
    
    last_solution = FileService.get_last_solution()

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    WebService.init(driver)
    solved_data = WebService.get_recent_solved_problem(driver, last_solution)
    print(len(solved_data))

    driver.close()