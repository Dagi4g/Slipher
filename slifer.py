import sqlite3
from datetime import date

data_base = "slifer.db"

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

class Subject:
    """The function of this class is to make adding ,
    removing,asking and editing subject simple."""
    def __init__(self):
        ...

    # but first adding.
    def add_subject(self, data_base : str ,subject_name: list[str],today) -> None:
        conn  = sqlite3.connect(data_base)
        cursor = conn.cursor()

        formated_list_input = []
        for subject in subject_name:
            table_row = {"name" : subject.strip(), #remove any white space.
                         "today" : today,
                         "rating" : 3,
                         }
            formated_list_input.append(table_row)

        cursor.executemany("INSERT INTO subjects(name, last_seen,rating) VALUES(:name,:today,:rating)",formated_list_input)
        conn.commit()

subject_names = input("please enter the subject\n> ").split(",")
sub = Subject()
sub.add_subject(data_base ,subject_names,today)
print("subject added successfully")























"""

# input returns string ,so using string method "split" is possible.
# this makes it effective for users to enter multiple data at once.
subjects = input("please enter the subject\n> ").split(",")


# when .stripe is used the input is no longer a string,
# it will be a list in which the data base wouldn't accept and rises error
# the for loop is used to eliminate that.
data = []
for subject in subjects:
    table_row = {"name" : subject.strip(),
                 "today" : today,
                 "rating" : 4.6}
    data.append(table_row)

# subject_name,last_seen date and the ratings must be provided(the rating might show the diffuculty of the subject

cursor.executemany("INSERT INTO subjects(name, last_seen,rating) VALUES(:name,:today,:rating)",data)

conn.commit()
print("adding subject is completed succesfully")
"""
