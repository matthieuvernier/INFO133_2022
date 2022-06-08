#pip install mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  port=3306
)

cur = conn.cursor()

cur.execute("SHOW DATABASES")

for row in cur:
  print(row) 

cur.execute("CREATE DATABASE info133_2022")
cur.execute("USE info133_2022")
cur.execute("CREATE TABLE news (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(300), title VARCHAR(300), date DATE, content TEXT)")