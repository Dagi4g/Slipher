# Copyright 2025 Dagim                      #
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.                      # You may obtain a copy of the License at   #                                           #     http://www.apache.org/licenses/LICENSE-2.0                                        #
# Unless required by applicable law or agreed to in writing, software                   # distributed under the License is distributed on an "AS IS" BASIS,                     # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sqlite3

class InitEntity:
    """ A class that will be used to initalize the subject and topic class.

    typical usage:

        class ClassName(InitEntity):
            
            ...
    """
    def __init__(self, data_base: str) -> None:
        """ The database must be intialized first because it will be used later repetidly in the class. """
    # This try statment is used to privent injection attack.                                 
        try :
            self.data_base = data_base
            self.connection = sqlite3.connect(data_base)
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT 1")
        except sqlite3.Error as e:
            print(f"Database Connection error:{e}")
            self.connection = None
    

class DatabaseManager:
    """ This class  will read the schema file from database directory and executes the code. """
    def __init__(self, data_path: str ):
        self.data_path = data_path
        self.connection = None

    def connect(self) -> None:
        if not self.connection:
            self.connection = sqlite3.connect(self.data_path)
        return self.connection
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None # return it to its original value .

    def executescript(self,schema_file):
        with open(schema_file) as file:                 # Storing all the code in one sql file is simple for managing the data base.
            schema = file.read()
            conn = sqlite3.connect(self.data_path)
            cursor = conn.cursor()
            cursor.executescript(schema)
            # */ There will be 3 tables in a data base called slifer that store,subject, topic and subtopic. */ 
            conn.commit()
        print("The Data base created successfully")
