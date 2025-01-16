import sqlite3
from datetime import date

# right now i am not concerned about sql conjector attack but in future this will be fixed
data_base = "slifer.db"


# by storing all the code in one sql file it is simple to manage the data base.
# eventhough i want to have some beautiful user interface ,creating the table for subject,topic and subtopic in the start will help me identify usefull approaches
with open("create_slifer_database.sql") as f:
    tables = f.read()


# */ there will be 3 tables in a data base called slifer that store Greade,subject, topic and subtopic. */

conn  = sqlite3.connect(data_base)

cursor = conn.cursor()

# putting these all cursor commands in a variable will be easire but the sqlite3 database is flexable enough that i don't need that

cursor.executescript(tables)

conn.commit()
print("The Data base created successfully")
"""add subject first then ask for topics and subtopics smothlly"""

class Subject:
    """The function of this class is to make adding ,
    removing,asking and editing subject simple."""
    def __init__(self, data_base: str) -> None:
        """ the database must be intialized first because it will be used later repetidly in the class. """
        self.data_base = data_base
        self.connection = sqlite3.connect(data_base)
        self.cursor = self.connection.cursor()
        

    # but first adding.
    def add_subject(self,subject_name: list[str],today: str = date.today().isoformat()) -> None:
        formated_subject_input = [
                {"name" : subject.strip(), #remove any white space.
                 
                 "rating" : 3,
                 "today" : today,
                 } for subject in subject_name
                ]

        self.cursor.executemany("INSERT INTO subjects(name, last_seen,rating) VALUES(:name,:today,:rating)",formated_subject_input)
        self.connection.commit()

class Topic:
    """ The topic class has the same functionality as the subject class"""

    def __init__(self,data_base: str) -> None:
        """ because topic is manuplated in a data base
        the database must be provided"""
        self.data_base = data_base
        self.connection = sqlite3.connect(data_base)
        self.cursor = self.connection.cursor()
    # Nothing will change from subject class.
    # but because i wanted to process subject id in the class there is additional code.
    def add_topic(self,subject_name : str,topic_name: str,remember_me : str = date.today().isoformat(), last_seen: str = date.today().isoformat(),
                  rating = 3):
        extract = self.cursor.execute("SELECT subject_id FROM subjects WHERE name = (?)",subject_name)
        result = extract.fetchone()
        # reporting to the user that the subject is not found is better than showing the trackrace
        if result:
            subject_id = result[0]
        else:
            print(f"Subject doesn't exist")
        formated_topic_list = [
                {"subject_id" : subject_id,
                 "name" : topic.strip(),
                 "remember_me" : remember_me,
                 "last_seen" : last_seen,
                 "rating" : rating

                 }for topic in topic_name
                ]
        self.cursor.executemany("""INSERT INTO topics(subject_id,name,remember_me,last_seen,rating) VALUES(:subject_id,:name,:remember_me,:last_seen,:rating)""",formated_topic_list)
        self.connection.commit()


# THE TEST PEOGRAM
subject_names = input("please enter the subject\n> ").split(",")
sub = Subject(data_base)
sub.add_subject(subject_names)
print("subject added successfully")

topic_name = input(f"add topics to {subject_names}\n> ").split(",")
top = Topic(data_base)
top.add_topic(subject_names,topic_name)





