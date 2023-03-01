import sqlite3
import requests
import re
from bs4 import BeautifulSoup

conn = sqlite3.connect("People1.db")
cursor = conn.cursor()

cursor.execute("SELECT name, category FROM Person")
rows = cursor.fetchall()


surnames =[]

for row in rows:
    full_name = row[0]
    category = row[1]

        
    if ',' in full_name:
        surname = full_name.split(',')[0].split()[-1]
    else:
        surname = full_name.split()[-1]

    if surname in surnames:
        continue

    else:
        surnames.append(surname)
        
        page = requests.get("".join(["https://apl.unob.cz/SearchPeople/Home/Index/cz?partname=", surname]))
        soup = BeautifulSoup(page.content, 'html.parser')

        for tr in soup.find_all('tr'):
            td = tr.find_all('td')
            if td:
                href = tr.find("td").find("a")["href"]
                number = int(re.search(r'/SearchPeople/Home/Detail/cz/(\d+)', href).group(1))
                department = td[1].text.strip()
                print(number, department, surname)
                #cursor.execute("""UPDATE Person SET category = ? WHERE store_id = ?; """, (department, number))
                #conn.commit() 

conn.close()

