# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 14:01:59 2024

@author: HP
"""
# Importing libraries
from selenium import webdriver
from selenium.webdriver import ActionChains
# Importing libraries to send input to the text box
from selenium.webdriver.common.keys import Keys
import time
# Wait time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# getting driver
cService = webdriver.ChromeService(executable_path='C:/Users/HP/Downloads/scraping/chromedriver.exe')
driver = webdriver.Chrome(service = cService)

# Entering the link
driver.get('https://www.google.com/')
time.sleep(2)
# Maximize the window
driver.maximize_window()
# Getting the input box by xpath
input_box = driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
input_box.send_keys('Ipl 2024 stats')
time.sleep(2)
input_box.send_keys(Keys.ENTER)

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'JglY8e')))

# Clicking the top link
driver.find_element('xpath', '/html/body/div[4]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a/div/div/div/div[1]/span').click()
time.sleep(2)
# Clicking Cookies button
driver.find_element('xpath', '/html/body/div[3]/div/button').click()

# Clicking View More Button
view_more = WebDriverWait(driver, 10).until(
     EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/div/a')))
actions = ActionChains(driver)
actions.move_to_element(view_more)
actions.click(view_more)
actions.perform()
    
time.sleep(2)
driver.execute_script('window.scrollTo(document.body.scrollHeight,250)')    




# Scraping the Data

#getting headers
headers = driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/div/section/div/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/table/tbody/tr[1]')
heads = []
for i in headers.find_elements(By.TAG_NAME, 'th'):
    heads.append(i.text)

import pandas as pd

df = pd.DataFrame(columns = heads)

tbody = driver.find_element(By.TAG_NAME, 'tbody')

all_row_values = []
for i in tbody.find_elements(By.TAG_NAME, 'tr')[1:]:
    row_values = []
    for j in i.find_elements(By.TAG_NAME, 'td'):
        row_values.append(j.text)
    all_row_values.append(row_values)
    
for i in all_row_values:
    df.loc[len(df)] = i

df.to_csv('output.csv', index=False)