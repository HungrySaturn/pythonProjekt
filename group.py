import requests
import re
from bs4 import BeautifulSoup
import sqlite3

# načte web stranky z txt souboru
with open('data.txt', 'r') as file:
    websites = file.readlines()

conn = sqlite3.connect("People1.db")
cursor = conn.cursor()

for website in websites:
    # stahne obsah z webu
    html_content = requests.get(website.strip()).text
    soup = BeautifulSoup(html_content, 'html.parser')

    department = ''
    number = 0

    for tr in soup.find_all('tr'):
        td = tr.find_all('td')
        if td:
            href = tr.find("td").find("a")["href"]
            number = int(re.search(r'/SearchPeople/Home/Detail/cz/(\d+)', href).group(1))
            department = td[1].text.strip()
            print(number, department)
            #cursor.execute("""UPDATE Person SET group1 = ? WHERE store_id = ?; """, (department, number))
            conn.commit()

conn.commit()

conn.close()



