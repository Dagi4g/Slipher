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
data_base = "/data/data/com.termux/files/home/slifer/App/Backend/DataBase/slifer.db"
schema_file = "/data/data/com.termux/files/home/slifer/App/Backend/DataBase/schema.sql"

# Eventhough i want to have some beautiful user interface ,creating the table for subject,topic and subtopic in the start will help me identify usefull approaches


""" Add subject first then ask for topics and subtopics smothlly"""

class Subject(InitEntity):
    " Subject class inherits from InitEntity class to initialize itself """
    def add_subject(self,subject_name: list[str],today: str = date.today().isoformat()) -> None:
        if not self.connection:
            print("Cannot add subject: database connection error")
            return
        
        formated_subject_input = [
                {"name" : subject.strip(), # Remove any white space.
                 
                 "rating" : 3,
                 "today" : today,
                 } for subject in subject_name
                ]
        try : 
            self.cursor.executemany("INSERT INTO subjects(name, last_seen,rating) VALUES(:name,:today,:rating)",formated_subject_input)
            print("Subject added succesfully.")
        except sqlite3.IntegrityError:
            print(f"{subject_name} exists in the database.")
        self.connection.commit()# because the bug only occur in execute many class every thing must be commited to privent locking the database.

    def edit_subject(self,existing_subject,edited):
        if self._check_subject(existing_subject):
            if not self._check_subject(edited):# Check if the new subject exists .
                self.cursor.execute("UPDATE subjects SET name = ? WHERE name = ?",(edited,existing_subject))
                print(f"{existing_subject} is sucessfully coverted to {edited}")
            else: # the new subject exists .
                print(f"{edited} already exists.")
        else:
            print(f"{existing_subject} doesn't exist") # This way the user wouldn't get error messages .

        self.connection.commit()


    def _check_subject(self,existing_subject: str)-> bool:
        check = self.cursor.execute("SELECT 1 FROM subjects WHERE name = ?",(existing_subject,)).fetchall() # Selecting one is enough for checking if it exists .
        # If the execute command wasn't fetched check will store empty list. 

        if check :# Exists.
            return True
        else :# Doesn't exist .
            return False

    def delete_subject(self,subject_name: str):
        if self._check_subject(subject_name):
            self.cursor.execute("DELETE FROM subjects WHERE name = ?",(subject_name,)) 
            self.connection.commit()
            print(f"{subject_name} successfully deleted")
        else:
            print(f"'{subject_name}' doesn't exist!")



    def close_connection(self):# In case if needed.
        self.connections().close()


