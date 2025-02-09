# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");


import sqlite3
from datetime import date

from initentity import InitEntity

# Right now i am not concerned about sql conjector attack but in future this will be fixed

# Eventhough i want to have some beautiful user interface ,creating the table for subject,topic and subtopic in the start will help me identify usefull approaches



class Subject(InitEntity):
    """ Handles  Subject related database opperations. """

    def add_subject(self,subject_name: list[str],today: str = date.today().isoformat()) -> None:
        if not self.connection:
            print("Cannot add subject: database connection error")
            return
        for subject in map(str.strip,subject_name):
            if not self._check_subject(subject):
                self._execute("INSERT INTO subjects(name,rating) VALUES (?,?)",(subject,3))
                print(f"subejct: '{subject}' added succesfully")
            else:
                print(f"'{subject}' already exists")


    def edit_subject(self,existing_subject,edited):
        if self._check_subject(existing_subject):
            if not self._check_subject(edited):# Edit if the new subject doesn't exists .
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


