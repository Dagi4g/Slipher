# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");

"""Managing subject-related database operations.

This module provides the `Subject` class , which allows  adding, editing, and deleting subject from database.(showing subject is not implemented yet).
Usage :
    foo = Subject(data_base_path)
    foo.add_subject(subject_name)
        # adds subject to the database.
    foo.edit_subject(old_subject,new_subject)
        # edits an existing subject in the database.
    foo.delete_subject(subject_name)
        # deletes the subject from the database.

"""

import sqlite3
from datetime import date

from initentity import InitEntity



class Subject(InitEntity):
    """ Handles  Subject related database opperations. """

    def add_subject(self,
                    subject_name: list[str],
                    today: str=date.today().isoformat()) -> None:
        if not self.connection:
            print("Cannot add subject: database connection error")
            return
        for subject in map(str.strip,subject_name):
            if not self._check_subject(subject):
                self._execute("INSERT INTO subjects(name,rating) VALUES (?,?)",(subject,3))
                print(f"subejct: '{subject}' added succesfully")
            else:
                print(f"'{subject}' already exists")


    def edit_subject(self,old_subject,new_subject):
        if self._check_subject(old_subject):
            if not self._check_subject(new_subject):# Edit if the new subject doesn't exists .
                self._execute("UPDATE subjects SET name = ? WHERE name = ?",(new_subject,old_subject))
                print(f"{old_subject} is sucessfully coverted to {new_subject}")
            else: # the new subject exists .
                print(f"{new_subject} already exists.")
        else:
            print(f"{old_subject} doesn't exist") # This way the user wouldn't get error messages .

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
            print(f"'{subject_name}' successfully deleted")
        else:
            print(f"'{subject_name}' doesn't exist!")

    def show_subject(self) -> str:
        """Show all the name of the subject with alphbetical order."""
        subjects = self.connection.execute("SELECT name FROM subjects ORDER BY name").fetchall()
        if len(subjects) > 0:
            for i,subject in enumerate(subjects,start=1):
                print(f"{i}, {subject[0]}")
        else:
            print("there is no subject in the database.")

