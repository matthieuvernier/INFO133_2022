#pip install mariadb
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="classicmodels"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Execute SQL command
cur.execute("show tables")

# Show results
for row in cur:
    print(row)

cur.execute("SELECT * FROM employees LIMIT 5")
for row in cur:
    print(row)