# Copyright 2025 Dagim                  
#
# Licensed under the Apache License, Version 2.0 (the "License");

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
    

def initalize_database(data_base: str, schema_file: str):
    """ This method will read the schema file from database directory and executes the code. """
    with open(schema_file) as file:                 # Storing all the code in one sql file is simple for managing the data base.
        schema = file.read()
        conn = sqlite3.connect(data_base)
        cursor = conn.cursor()
        cursor.executescript(schema)
        # */ There will be 3 tables in a data base called slifer that store,subject, topic and subtopic. */ 
        conn.commit()
        print("The Data base created successfully")
