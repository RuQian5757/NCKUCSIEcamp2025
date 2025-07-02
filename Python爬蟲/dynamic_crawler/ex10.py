from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 隱式等待
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 最多等 10 秒
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime")

search_station = driver.find_element(By.XPATH, '//*[@id="queryForm"]/div/div[1]/div[1]/div[2]/a[2]')  # 自動最多等 10 秒直到出現
search_station.click()

time.sleep(5)
driver.quit()

print("-" * 10 + "我是分割線" + "-" * 10)

# 顯式等待
driver = webdriver.Chrome()
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime")

# return WebElement
query_station = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="queryForm"]/div/div[1]/div[1]/div[2]/a[2]'))
)

# return WebElement
query_condition = WebDriverWait(driver, 10).until(
    EC.any_of(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="queryForm"]/div/div[1]/div[1]/div[2]/a[2]')),
        EC.element_to_be_clickable((By.XPATH, '//*[@id="queryForm"]/div/div[1]/div[1]/div[2]/a[3]'))
    )
)

# return list of WebElement
query_conditions = WebDriverWait(driver, 10).until(
    EC.all_of(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="queryForm"]/div/div[1]/div[1]/div[2]/a[2]')),
        EC.element_to_be_clickable((By.XPATH, '//*[@id="queryForm"]/div/div[1]/div[1]/div[2]/a[3]'))
    )
)

query_condition .click()

time.sleep(5)
driver.quit()