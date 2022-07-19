import sqlite3

conn = sqlite3.connect('test.db')

conn.execute(""" 
CREATE TABLE IF NOT EXISTS PASSWORDS 
(ID INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,
WEBSITE      TEXT       NOT NULL,
PASSWORD     TEXT       NOT NULL);
""")

conn.close()

def Save_data(website, password):
    conn = sqlite3.connect('test.db')
    conn.execute("INSERT INTO PASSWORDS (WEBSITE, PASSWORD) \
      VALUES (?,?)", (website, password))
    conn.commit()
    
    conn.close()

def Retrive_data(website):
    conn = sqlite3.connect('test.db')
    cursor = conn.execute("SELECT WEBSITE, PASSWORD from PASSWORDS WHERE WEBSITE LIKE '" + website + "'")
    for row in cursor:
        conn.close()
        return row[0], row[1]

def Retrive_all_data():
  conn = sqlite3.connect('test.db')
  cursor = conn.execute("SELECT * from PASSWORDS")
  for row in cursor:
    print(row[1], row[2])
  conn.close()

def delete_data(website):
  conn = sqlite3.connect('test.db')
  conn.execute("DELETE from PASSWORDS where WEBSITE LIKE '" + website + "'")
  conn.commit()
  conn.close()
