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
    courses = courses_div.find_all("div", class_="accordion-item")

    i = 1
    for course in courses:
        course_name = ' '.join(course.button.text.split())
        print(f"第 {i} 門課 : {course_name}")

        contents = course.find_all("li")
        for content in contents:
            print(" - " + content.text)
        i += 1
        print()


soup.find("div", class_= "class_name", id="id_name", style="style_name")