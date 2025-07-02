import requests
from bs4 import BeautifulSoup as bs

url = "https://www.cwa.gov.tw/V8/C/W/Town/Town.html?TID=6300100"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=5) 

# 可將產生的檔案拉到瀏覽器預覽抓取到啥
with open("debug.html", "w", encoding="utf-8") as f:
    f.write(response.text)

