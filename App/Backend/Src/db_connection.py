# Copyright 2025 Dagim                  
#
# Licensed under the Apache License, Version 2.0 (the "License");
import os
import sys
import sqlite3

def initalize_database(data_base: str, schema_file: str):
    """ This method will read the schema file from database directory and executes the code. """
    if not os.path.exists(data_base):
        print(f"database {data_base} not found.\nThis error occurs when the config.py has wrong path to the database, or the database file doesn't exist.")
        sys.exit()
        

    try:
        with open(schema_file) as file:                 # Storing all the code in one sql file is simple for managing the data base.
            schema = file.read()
            conn = sqlite3.connect(data_base)
            cursor = conn.cursor()
            cursor.executescript(schema)
            # */ There will be 3 tables in a data base called slifer that store,subject, topic and subtopic. */ 
            conn.commit()
    except FileNotFoundError:
        print("Error: schema file not found.\nThis error occurs when the config.py has wrong path to the schema.sql.")
        sys.exit()
