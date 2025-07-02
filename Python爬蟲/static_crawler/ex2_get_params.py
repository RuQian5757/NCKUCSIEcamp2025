import requests
from bs4 import BeautifulSoup as bs

url = "https://www.ptt.cc/bbs/movie/search"
params = {
    "q": "動作"  
}
response = requests.get(url, params=params)
print("Current url :", response.url)
print()

# 輸出內文 (可忽略)

response = requests.get(url, params=params)
soup = bs(response.text, "html.parser")

if response.status_code == 200:
    html = response.text

    contents = soup.find_all("div", class_="r-ent")

    for i, content in enumerate(contents, 0):
        title_tag = content.find("div", class_="title").find("a")
        if title_tag:
            title = title_tag.text.strip()
            print(title)
        else:
            title = "(本文已被刪除)"
            link = "(無連結)"
else:
    print("請求失敗", response.status_code)
