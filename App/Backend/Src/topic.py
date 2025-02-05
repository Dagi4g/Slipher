# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");

import sqlite3
from datetime import date

from init_db_connection import InitEntity,initalize_database


class Topic(InitEntity):
    """ A class for managing topic """
    def add_topic(self,subject_name : str,topic_name: str,remember_me : str = date.today().isoformat(), last_seen: str = date.today().isoformat(),
                  rating = 3):
        self._get_subject_id(subject_name)
        formated_topic_list = [
                {"subject_id" : self.subject_id,
                 "name" : topic.strip(),
                 "remember_me" : remember_me,
                 "last_seen" : last_seen,
                 "rating" : rating

                 }for topic in topic_name
                ]
        try :
            self.cursor.executemany(
    """
    INSERT INTO topics(subject_id,name,remember_me,last_seen,rating) 
    VALUES(:subject_id,:name,:remember_me,:last_seen,:rating)""",formated_topic_list)
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



        """check_topic = self._check_topic(previous_topic,self.subject_id)
        
        if check_topic:
            self.cursor.execute("UPDATE topics SET name = ? WHERE name = ? AND subject_id = ?",(new_topic,previous_topic,self.subject_id))
            self.connection.commit()
            print(f"{previous_topic} succesfully changed to {new_topic}")
        else:
            print(f"{subject_name} doesn't have {previous_topic} topic")"""


    def _check_topic(self,topic_name: str)-> bool:

        check = self.connection.execute("SELECT 1 FROM topics WHERE name = ? AND subject_id = ?",(topic_name,self.subject_id)).fetchall()
        if check : # Exists.
            return True
        else: # Doesn't Exist.
            return False

    def delete_topic(self,subject_name: str,topic_name: str) -> None:
        if self._get_subject_id(subject_name):
            if self._check_topic(topic_name,self.subject_id):
                self.cursor.execute("DELETE FROM topics WHERE name = ?",(topic_name,))
                print(f"'{topic_name}' succesfully deleted")
                self.connection.commit()
            else:
                print(f"topic: '{topic_name}' doesn't exist")
        else :
            print(f"subject: '{subject_name}' doesn't exist")







