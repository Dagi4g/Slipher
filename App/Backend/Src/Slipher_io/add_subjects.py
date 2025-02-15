# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def add_subjects(subject_handler):
    """ Handles user input for adding subjects."""
    subject_names = input("Enter subjects (comma-separated):\n> ").split(",")
    subject_names = [s.strip() for s in subject_names if s.strip()]
    if subject_names:
        subject_handler.add_subject(subject_names)
        # There is no need for printing subject is added because the subject_handler have to care about that.
