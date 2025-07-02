from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime")

time.sleep(10)
driver.quit()

