# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");


# every method of this class can be used anywhere once it is initalized to a database.

import sqlite3
from datetime import date

from initentity import InitEntity

class Topic(InitEntity):
    """ A class for managing topic """
    def add_topic(
            self,subject_name : list[str],
            topic_name: str,
            last_seen: str = date.today().isoformat(),
            rating : int = 3):
        self._get_subject_id(subject_name)
        formated_topic_list = [
                {"subject_id" : self.subject_id,
                 "topic_name" : topic.strip(),
                 "last_seen" : last_seen,
                 "rating" : rating

                 }for topic in topic_name
                ]
        try :
            self.cursor.executemany(
    """
    INSERT INTO topics(subject_id,name,last_seen,rating) 
    VALUES(:subject_id,:topic_name,:last_seen,:rating)""",formated_topic_list)
            print("topic added successfully.")
        except sqlite3.IntegrityError:
            print(f"topic: {topic_name} exists.")
        self.connection.commit()

    def _get_subject_id(self, subject_name: str) -> int:
        self.subject_id = 0 # I will this value through out the entire class
        subject = (subject_name.strip(),)
        extract = self.cursor.execute("SELECT subject_id FROM subjects WHERE name = ?",subject) # i used brackets to put ? sign but when i tried to use add_topic the code raised "incorrect number of binding suplied error.
        result = extract.fetchone()
        # reporting to the user that the subject is not found is better than showing the trackrace
        if result:
            self.subject_id = result[0]
            return True
        else:
            return False
 

    def edit_topic(self,subject_name: str,previous_topic: str, new_topic: str ) -> None:
        if self._get_subject_id(subject_name): # Verify the existence of subject before editing topic .
            if self._check_topic(previous_topic): # Varify the existance of topic.
                self.cursor.execute("UPDATE topics SET name = ? WHERE name = ? AND subject_id = ?",(new_topic,previous_topic,self.subject_id))
                self.connection.commit()
                print(f"{previous_topic} succesfully changed to {new_topic}")
            else:
                print(f"{subject_name} doesn't have {previous_topic} topic")



    def _check_topic(self,topic_name: str)-> bool:

        check = self.connection.execute("SELECT 1 FROM topics WHERE name = ? AND subject_id = ?",(topic_name,self.subject_id)).fetchall()
        if check : # Exists.
            return True
        else: # Doesn't Exist.
            return False

    def delete_topic(self,subject_name: str,topic_name: str) -> None:
        if self._get_subject_id(subject_name):
            if self._check_topic(topic_name):
                self.cursor.execute("DELETE FROM topics WHERE name = ?",(topic_name,))
                print(f"'{topic_name}' succesfully deleted")
                self.connection.commit()
            else:
                print(f"topic: '{topic_name}' doesn't exist")
        else :
            print(f"subject: '{subject_name}' doesn't exist")


    def show_topics(self) -> None:
        """Ask the user to chose subject from database by showing them all subjects with respect to there id.

        Then take the id of the subject and show all the topics in alphabetical order"""
        subjects = self.connection.execute("SELECT subject_id ,name FROM subjects ORDER BY subject_id").fetchall() # instead of showing all the topics ,just show topics from which the user chose the subject.

        if len(subjects) > 0:
            for subject_id , name in subjects:
                print(f"{subject_id}, {name}") # just show all the topics at once.
            chose_id = input("enter the id of the subject to see its topics:\n> ")
            if chose_id:
                # The user chosen an id.
                topics = self.connection.execute("SELECT name FROM topics WHERE subject_id = ?",(chose_id,)).fetchall()
                if len(topics) > 0:
                    for i,topic_name in enumerate(topics,start=1):
                        print(f"{i}, {topic_name[0]}")
                else:
                    subject_name = self.connection.execute("SELECT name FROM subjects WHERE subject_id = ?",(chose_id,)).fetchone()
                    print(f"subject: '{subject_name[0]}' doesn't have topics.")
        else: 
            print("there is no subject in the database")

            ...
