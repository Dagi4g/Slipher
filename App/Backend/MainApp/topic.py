# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sqlite3
from datetime import date

from init_db_connection import InitEntity,initalize_database

# Right now i am not concerned about sql conjector attack but in future this will be fixed

# Eventhough i want to have some beautiful user interface ,creating the table for subject,topic and subtopic in the start will help me identify usefull approaches


class Topic(InitEntity):
    """ A class for managing topic """
    def add_topic(self,subject_name : str,topic_name: str,remember_me : str = date.today().isoformat(), last_seen: str = date.today().isoformat(),
                  rating = 3):
        subject_id = self._get_subject_id(subject_name)
        formated_topic_list = [
                {"subject_id" : subject_id,
                 "name" : topic.strip(),
                 "remember_me" : remember_me,
                 "last_seen" : last_seen,
                 "rating" : rating

                 }for topic in topic_name
                ]
        try :
            self.cursor.executemany("""INSERT INTO topics(subject_id,name,remember_me,last_seen,rating) VALUES(:subject_id,:name,:remember_me,:last_seen,:rating)""",formated_topic_list)
            print("topic added successfully.")
        except sqlite3.IntegrityError:
            print(f"{topic_name} exists in the database")
        self.connection.commit()

    def _get_subject_id(self, subject_name: str) -> int:
        subject = (subject_name.strip(),)
        extract = self.cursor.execute("SELECT subject_id FROM subjects WHERE name = ?",subject) # i used brackets to put ? sign but when i tried to use add_topic the code raised "incorrect number of binding suplied error.
        result = extract.fetchone()
        # reporting to the user that the subject is not found is better than showing the trackrace
        if result:
            return result[0]
        else:
            print(f"Subject doesn't exist")
 

    def edit_topic(self,subject_name: str,previous_topic: str, new_topic: str ) -> None:
        subject_id = self._get_subject_id(subject_name)
        check_topic = self._check_topic(previous_topic,subject_id)
        
        if check_topic:
            self.cursor.execute("UPDATE topics SET name = ? WHERE name = ?",(new_topic,previous_topic))
            self.connection.commit()
            print(f"{previous_topic} succesfully changed to {new_topic}")
        else:
            print(f"{subject_name} doesn't have {previous_topic} topic")

        """ inorder to edit the topic i need the id of the subject and the look for the topic in that subject .using this sql command ("SELECT name FROM topics WHERE subject_id = ?",subject_id).
        i also need to know the topic i am editing doesn't belong to another subject.
        how :
            one way to do that is first checking if the topic is from the subject and editing it else printing the subject doesn't have any topic they provided.
        for this i need:
            - a method to check for subject , existance of topic in paticular subject.
           the edit  """


    def _check_topic(self,topic_name: str,subject_id)-> bool:

        check = self.connection.execute("SELECT 1 FROM topics WHERE name = ? AND subject_id = ?",(topic_name,subject_id)).fetchall()
        if check : # Exists.
            return True
        else: # Doesn't Exist.
            return False





