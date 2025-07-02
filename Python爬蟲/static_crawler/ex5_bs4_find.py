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
    courses_div = soup.find("div", class_="space-y-4 bg-white bg-opacity-80 p-6 rounded-lg")
    first_course = courses_div.find("div", class_="accordion-item")
    course_name = ' '.join(first_course.button.text.split()) #清除文字中的空格
    print(f"第 1 門課：{course_name}")

    course_contents = first_course.find_all("li")
    for content in course_contents:
        print(" - " + content.text)
