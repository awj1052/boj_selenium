from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import FileService, WebService, FilterService

if __name__ == "__main__":

    try:
        target = int(input("Enter the problem number : "))
    except:
        print("Enter the problem number.")
        exit()
    
    last_solution = FileService.get_last_solution()

    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_service = webdriver.ChromeService('/usr/lib/chromium-browser/chromedriver')
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

    print("Starting the WebService..")
    WebService.init(driver, target)
    print("Getting Info..")
    solved_data = WebService.get_recent_solved_problem(driver, last_solution)
    print("Filtering problem numbers..")
    filtered_data = FilterService.filtering_problem_number(solved_data, target)
    print("Getting usernames..")
    usernames = FilterService.get_usernames(filtered_data)
    print("Get Results")
    print(*usernames)
    print()
    
    #names = FileService.get_name(usernames)
    #print(*names)

    driver.close()
