from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime")

#獲取起始站與終點站的元素
start_station = driver.find_element(By.ID, 'startStation')
end_station = driver.find_element(By.ID, 'endStation')

#填入資料
start_station.send_keys('4400-高雄')
end_station.send_keys('4220-臺南')

#找到查詢按鈕後按下去
submit_btn = driver.find_element(By.XPATH, '//*[@id="queryForm"]/div/div[3]/div[3]/input')
submit_btn.click()

time.sleep(20)
driver.quit()