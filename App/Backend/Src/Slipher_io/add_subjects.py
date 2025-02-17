# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def add_subjects(subject_handler):
    """ Handles user input for adding subjects."""
    subject_names = input("Enter subjects (comma-separated):\n> ").split(",")
    subject_names = [s.strip() for s in subject_names if s.strip()]
    if not subject_handler._check_subject(subject_name) :
        subject_handler.add_subject(subject_names)
if not self._check_subject(subject):                                                  self._execute("INSERT INTO subjects(name,rating) VALUES (?,?)",(subject,3))                                                print(f"subejct: '{subject}' added succesfully")                              else:                                        print(f"'{subject}' already exists")
