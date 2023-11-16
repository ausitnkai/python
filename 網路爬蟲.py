from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PATH = "C:/Users/hhh12/OneDrive/Desktop/chromedriver-win64/chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://ani.gamer.com.tw/")

#搜尋東西
search = driver.find_element(By.NAME, 'keyword')
search.clear()
search.send_keys("刀劍神域")
search.send_keys(Keys.RETURN)

#等待頁面跳轉
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "theme-title"))
)

#取得標題
titles = driver.find_elements(By.CLASS_NAME, "theme-name")
for title in titles:
   print(title.text)

#點擊連結操作
link = driver.find_element(By.CLASS_NAME, 'theme-list-main')
link .click()

driver.back()#回到上一頁
driver.forward()#回到下一頁

time.sleep(7)
driver.quit()