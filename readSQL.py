#store_id INTEGER PRIMARY KEY, category TEXT, group1 TEXT, email TEXT, phone TEXT
#program na čtení dat z databáze


import sqlite3

# připojení k databázi
conn = sqlite3.connect("People1.db")

# vytvoření kurzoru
cursor = conn.cursor()

# výběr dat z databáze

#cursor.execute("SELECT * FROM Person") #4325 lidí celkem

#cursor.execute("SELECT * FROM Person WHERE category = 'NÚKIB' ") # 40ks lidí z NÚKIBu 

#cursor.execute("SELECT name,category,group1 FROM Person WHERE name LIKE '%(ček.)%'") #1402 vojenských studentů

#cursor.execute("SELECT name,category,group1 FROM Person WHERE category LIKE '%Magisterský studijní program%'") # 1525 studentů magistra + navazujícího mgr 
#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%Bakalářský studijní program%'")# 177 studentů bc
#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%Doktorský studijní program%'")# 119 studentů doktorského s.
#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%studijní program%'") #1820 - 1 člověk má uvedeno Mgr i Bc

#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%Kurz vyšších důstojníků%'")# 53 lidí

#cursor.execute("SELECT name,category, group1 FROM Person WHERE category LIKE '%Odborný kurz%'AND name NOT LIKE '%(ček.)%'") #55 nestudentů na odborném kurzu 
#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%Jazykový kurz%'") #269 lidí

#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%Rektorát%'") #239 lidí

#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%Školní pluk%'") #67 lidí

#cursor.execute("SELECT name,category FROM Person WHERE category LIKE '%Fakulta%'") # 493 lidí, výzkumní pracovníci?
#cursor.execute("SELECT * FROM Person WHERE phone != 'None'") #936, počet lidí s telefonem
#cursor.execute("SELECT * FROM Person WHERE group1 LIKE '%KB%'")

#cursor.execute("SELECT * FROM Person WHERE name LIKE '%Ráčil%'")

rows = cursor.fetchall()

i = 0 #počty

#tisk dat
for row in rows:
    
    print(row)
    i+=1
    
print(i)

#uzavření spojení
conn.close()


