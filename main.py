
import requests
from bs4 import BeautifulSoup
import re
import sqlite3



conn = sqlite3.connect("People1.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Person(store_id INTEGER PRIMARY KEY, name TEXT, category TEXT, group1 TEXT, email TEXT, phone TEXT)");


class Person:
    def __init__(self, ID, name, category, group1, email, phone):
        self.ID = ID
        self.name = name
        self.category = category
        self.group1 = group1
        self.email = email
        self.phone = phone
        

email_id = re.compile('\w+@\w+.\w+')
phone_id = re.compile(r'\d{3} \d{3} \d{3}')




def get_data(b):
        
    page = requests.get("".join(["https://apl.unob.cz/SearchPeople/Home/Detail/cz/", str(b)]))
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_phone(soup):

    phone = soup.find(text=phone_id)
    if phone is not None:
        return phone.text.strip()
    return 'None'

def get_email(soup):
    
    email = soup.find(text=email_id)
    if email is not None:
        return email.strip()
    else:
        return 'None'
    

def get_name(soup):

    td_element = soup.select_one("td:nth-of-type(3)")
    if td_element is not None:
        return td_element.text.strip()



def insert_data(person):
    #cursor.execute("INSERT INTO Person (store_id, name, category, group1, email,phone) VALUES (?, ?, ?, ?, ?,?)", (person.ID, person.name, person.category, person.group1, person.email,person.phone))
    print(person.ID, person.name, person.category, person.group1, person.email, person.phone)
        


def process_data(a):
    soup = get_data(a)
    name = get_name(soup)
    if name is not None:
        phone = get_phone(soup)
        email = get_email(soup)
        category = 'None'
        group1 = 'None'
        person = Person(a, name, category, group1, email,phone)
        insert_data(person)
        

        
for i in range(30,100):
    process_data(i)
    #conn.commit();
    #print(i)

conn.commit();
conn.close();


'''
import threading
import requests
from bs4 import BeautifulSoup
import re
from functools import cache
import sqlite3
import concurrent.futures



conn = sqlite3.connect("People.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Person(store_id INTEGER PRIMARY KEY, name TEXT, category TEXT, group1 TEXT, email TEXT)");


class Person:
    def __init__(self, ID, name, category, group1, email):
        self.ID = ID
        self.name = name
        self.category = category
        self.group1 = group1
        self.email = email
        

email_id = re.compile('\w+@\w+.\w+')
phone_id = re.compile(r'\d{3} \d{3} \d{3}')


lock = threading.Lock()

@cache
def get_data(b):
    with lock:
        # Access shared resources within the lock
        page = requests.get("".join(["https://apl.unob.cz/SearchPeople/Home/Detail/cz/", str(b)]))
        soup = BeautifulSoup(page.content, 'html.parser')
    return soup

def get_phone(soup):
    with lock:
        phone = soup.find(text=phone_id)
    if phone is not None:
        return phone.text.strip()
    return 'None'

def get_email(soup):
    with lock:
        # Access shared resources within the lock
        email = soup.find(text=email_id)
    if email is not None:
        return email.strip()
    else:
        return 'None'
    

def get_name(soup):
    with lock:
        # Access shared resources within the lock
        td_element = soup.select_one("td:nth-of-type(3)")
    if td_element is not None:
        return td_element.text.strip()



def insert_data(person):
    with lock:
        cursor.execute("INSERT INTO Person (store_id, name, category, group1, email) VALUES (?, ?, ?, ?, ?)", (person.ID, person.name, person.category, person.group1, person.email))

        


def process_data(a):
    soup = get_data(a)
    name = get_name(soup)
    if name is not None:
        #phone = get_phone(soup)
        email = get_email(soup)
        category = 'None'
        group1 = 'None'
        person = Person(a, name, category, group1, email)
        insert_data(person)
        

        
for i in range(2800,2830):
    process_data(i)



with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(process_data, range(2800, 2900))


conn.commit();
conn.close();

'''
