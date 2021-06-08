user_Name = input('Enter your Username : ')
pass_Word = input('Enter your Password : ')


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget

driver = webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
#driver = webdriver.Edge('E:\Programming_Stuff\Selenium_WebScraping\EdgeDriver\msedgedriver.exe')
driver.get('https://www.instagram.com/')


username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

username.send_keys(user_Name)
password.send_keys(pass_Word)


log_in = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
not_now = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
not_now2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Not Now')]"))).click()
driver.get('https://www.instagram.com/{}/saved'.format(user_Name))
counter = 0
while True:
    try:
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='_9AhH0']"))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Remove']"))).click()
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Close']"))).click()
        counter+=1
        driver.refresh()
    except:
        print('Finished. Total Unsaved Items : '+str(counter))
        break