import requests
from bs4 import BeautifulSoup as bs

url = "https://sunnyshoun.github.io/2025-NCKUCSIE-camp"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers, timeout=5) 
soup = bs(response.text, "html.parser")

if response.status_code == 200:
    print(soup.head)
    print()
    print("-" *10 + "我是分割線" + "-" *10)
    print()
    print(soup.nav)
    print()
    print("-" *10 + "我是分割線" + "-" *10)
    print()
    print(soup.section)
    print()
    print("-" *10 + "我是分割線" + "-" *10)
    print()
    print(soup.div)
    print()
    print("-" *10 + "我是分割線" + "-" *10)
    print()
    print(type(soup.div))
    print(soup.div.a)
    print()
    print("-" *10 + "我是分割線" + "-" *10)
    print()
    print(soup.div.ul)