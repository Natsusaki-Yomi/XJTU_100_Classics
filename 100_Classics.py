from time import sleep

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

username = input('Please input your NetID: ')
pwd = input('Please input your password: ')

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
browser = webdriver.Chrome(chrome_options=option)

browser.get('http://nsa.xjtu.edu.cn')
sleep(3)
browser.find_element(By.CLASS_NAME, 'username').send_keys(username)
browser.find_element(By.CLASS_NAME, 'pwd').send_keys(pwd)
browser.find_element(By.ID, 'account_login').click()
sleep(3)
for i in range(4):
    browser.find_element(By.XPATH, '//*[@id="fw"]/div/div[2]/div/div[1]/div[1]/div[1]/div/a[2]').click()
    sleep(5)
    browser.switch_to.window(browser.window_handles[1])
    browser.find_element(By.XPATH, '/html/body/div/div[1]/section/div/div[3]/ul/li[{}]'.format(i + 1)).click()
    sleep(3)
    eva = {}
    for index in range(25):
        label = browser.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/section/div/div[4]/div[{0}]/div[1]/div['
                                     '3]/table/tbody/tr[{1}]/td[2]'.format(
                                         i + 2, index + 1))
        t = browser.find_element(By.XPATH,
                                 '/html/body/div[1]/div[1]/section/div/div[4]/div[{0}]/div[1]/div[3]/table/tbody/tr[{'
                                 '1}]/td[8]'.format(
                                     i + 2, index + 1))
        eva[label.get_attribute('textContent')] = t.get_attribute('textContent')
    browser.find_element(By.XPATH,
                         '/html/body/div/div[1]/section/div/div[4]/div[{0}]/div[1]/div[2]/table/thead/tr/th['
                         '1]/div'.format(
                             i + 2)).click()
    browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/section/div/div[2]/div/button').click()
    sleep(10)
    texts = browser.find_elements(By.CLASS_NAME, 'el-textarea__inner')
    for index in range(len(texts)):
        texts[index].clear()
        name = browser.find_element(By.XPATH,
                                    '/html/body/div/div[1]/section/div/div[2]/div[1]/form[{}]/div[8]/div/div/span'.format(
                                        index + 1))
        texts[index].send_keys(eva[name.get_attribute('textContent')])
        save = browser.find_element(By.XPATH,
                                    '/html/body/div/div[1]/section/div/div[2]/div[1]/form[{}]/div[11]/button[1]'.format(
                                        index + 1))
        browser.execute_script('arguments[0].click();', save)
    sleep(2)
    submit = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/section/div/div[2]/div[2]/button[2]')
    browser.execute_script('arguments[0].click();', submit)
    sleep(2)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    sleep(2)
