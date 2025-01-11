import sqlite3
from datetime import date

today = date.today()
today = today.isoformat()

# by storing all the code in one sql file it is simple to manage the data base.
# eventhough i want to have some beautiful user interface ,creating the table for subject,topic and subtopic in the start will help me identify usefull approaches
with open("create_slifer_database.sql") as f:
    tables = f.read()


# */ there will be 3 tables in a data base called slifer that store Greade,subject, topic and subtopic. */

conn  = sqlite3.connect("slifer.db")

cursor = conn.cursor()

# putting these all cursor commands in a variable will be easire but the sqlite3 database is flexable enough that i don't need that

cursor.executescript(tables)

conn.commit()
print("The Data base created successfully")
"""add subject first then ask for topics and subtopics smothlly"""

subject = input("please enter the subject\n> ")

# subject_name,last_seen date and the ratings must be provided(the rating might show the diffuculty of the subject
data = (
        {"name" : subject,
         "today" : today,
         "rating" : 4.5},
        )

cursor.executemany("INSERT INTO subjects(name, last_seen,rating) VALUES(:name,:today,:rating)",data)

conn.commit()
subject_name = cursor.execute("SELECT * FROM subjects")
print(subject_name.fetchall())


