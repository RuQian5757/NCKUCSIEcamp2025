from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

"""
能將字串 "x小時y分鐘" 轉成以分鐘為單位的數字
"""
def convert_to_minutes(time_str):
    minutes = 0
    # 抓小時
    if "小時" in time_str:
        hour_part = time_str.split("小時")[0].strip()
        minutes += int(hour_part) * 60
        time_str = time_str.split("小時")[1]

    # 抓分鐘
    if "分" in time_str:
        min_part = time_str.split("分")[0].strip()
        if min_part:
            minutes += int(min_part)

    return minutes

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

# 等刷新後取得車輛 table
table = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="pageContent"]/div/table'))
)

# 取得table中的欄位
columns = table.find_elements(By.CSS_SELECTOR, "tr.trip-column")

i = 1
for column in columns:
    # 抓取欄位的資訊
    info = column.find_elements(By.TAG_NAME, "td")
    # 抓取行駛時間
    # info[3] 其實也就是 tr欄位下第4個td
    travel_time = convert_to_minutes(info[3].text)
    if(travel_time <= 40):
        print(f"選擇{i} : {info[0].text}")
        print(f"時間 : {info[1].text} ~ {info[2].text} ({travel_time} min)")
        print()
        i += 1

time.sleep(10)
driver.quit()