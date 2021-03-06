import sqlite3
from os.path import expanduser

sqlite_file = expanduser("~") + "/Desktop/data/db.sqlite"

connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

sql = "CREATE TABLE 2016KDDCupSelectedAffiliations \
          (id INTEGER PRIMARY KEY AUTOINCREMENT, \
          course TEXT, \
          author TEXT, \
          Cost INTEGER, \
          Date TEXT)"
# Creating a new SQLite table
cursor.execute(sql)
# Committing changes and closing the connection to the database file
connection.commit()
connection.close()

"""
# Adding records to table
`sql = "INSERT INTO Courses (course, author, Cost, Date) VALUES ('Algebra I','Math Fortress',10,'2014-01-14')"
`cursor.execute(sql)
sql = "INSERT INTO Courses (course, author, Cost, Date) VALUES ('Persuasive Presentations','Sharon Kroes',43,'2014-02-07')"
cursor.execute(sql)
# Committing changes and closing the connection to the database file
connection.commit()



# query and print the data
cursor.execute('select * from Courses')
for records in cursor.fetchall():
  print(records)




# editing
sql = "UPDATE Courses SET Date='2014-02-08' WHERE course='Persuasive Presentations'"
cursor.execute(sql)
# If the WHERE clause was omitted, that value would have been inserted into all of the records.
"""

"""
# deleting
sql = "DELETE FROM Courses WHERE id=1"
cursor.execute(sql)
"""
