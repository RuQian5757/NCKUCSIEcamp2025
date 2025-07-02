import requests
from bs4 import BeautifulSoup as bs

url = "https://sunnyshoun.github.io/2025-NCKUCSIE-camp"
response = requests.get(url)
print("status_code : ", response)
print(response.text)

