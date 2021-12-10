from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from os import environ, path
from dotenv import load_dotenv
import time
import os 
_isFinished = False


def searchLoopHandler(driver, times):
    numOfTimes = times
    while numOfTimes >= 0:
        driver.find_element(By.ID,'search').send_keys('Bitcoin')
        driver.find_element(By.XPATH,"//*[@id='search-input']/div/span").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"/html/body/div/div[2]/div[3]/div[1]/dic/div[1]/div/a").click()
        time.sleep(2)
        numOfTimes = numOfTimes - 1


if __name__ == '__main__':
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))
    email = environ.get('EMAIL')
    pwd = environ.get('PASSWORD')
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(
        '/home/user/Desktop/presearch_auto_search/chromedriver', options=options)
    driver.get("https://presearch.org/")
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,'Register or Login').click()
    driver.find_element(By.NAME,'email').send_keys(email)
    driver.find_element(By.NAME,'password').send_keys(pwd)
    while _isFinished == False:
        x = input("[Command]:")
        if (x == 'start'):
            searchLoopHandler(driver, 62)
        elif(x == 'close'):
            _isFinished = True
        else:
            pass
