from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime")

print(driver.find_element(By.CLASS_NAME, 'endStation'))
print(driver.find_element(By.ID, 'endStation'))
print(driver.find_element(By.NAME, 'endStation'))
print(driver.find_element(By.XPATH, '//*[@id="endStation"]'))

time.sleep(10)
driver.quit()