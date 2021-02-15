import sqlite3

# conn= sqlite3.connect("Employers.db")
# c = conn.cursor()
# c.execute("UPDATE points_and_income SET Income=0")

# conn.commit()
from datetime import date

print(date.today())

conn = sqlite3.connect("Employers.db")
c = conn.cursor()
d = conn.cursor()
c.execute("UPDATE employers SET Gender = 'Male' WHERE Name = 'Pouya' ")
d.execute("UPDATE points_and_income SET Gender = 'Male' WHERE Name = 'Pouya' ")


conn.commit()
