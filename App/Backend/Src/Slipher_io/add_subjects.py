# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

from .add_topics import add_topic

def add_subjects(subject_handler,topic_handler):
    """ Handles user input for adding subjects."""

    #Topic handler is neede incase the user wants to add topic to the subject.
    subject_names = input("Enter subjects (comma-separated) or 'q' to quit:\n> ").split(",")
    for i in subject_names :
        if i.lower() == "q":

            return
        
    subject_names = [s.strip() for s in subject_names if s.strip()]
    if subject_names:
        subject_handler.add_subject(subject_names)
    # ask the users if they want to add topics to this subject.
    for subject in subject_names:
        choice = input(f"do you want to add topic for \"{subject}\" (press enter) or quit(enter \"q\"):\n>")
        if choice.lower() == "q":
            return
        else:
            add_topic(topic_handler,subject)

                
            
