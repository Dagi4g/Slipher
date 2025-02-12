# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");

import sqlite3
from datetime import date

from initentity import InitEntity
from db_connection import initalize_database

from subject import Subject
from topic import Topic
from config import db_path, schema_file

def add_subjects(subject_handler):
    """ Handles user input for adding subjects."""
    subject_names = input("Enter subjects (comma-separated):\n> ").split(",")
    subject_names = [s.strip() for s in subject_names if s.strip()]
    
    if subject_names:
        subject_handler.add_subject(subject_names)

def edit_subject(subject_handler):
    existing_subject = input("Enter subject to rename:\n> ")
    if subject_handler._get_subject_id(existing_subject):
        new_subject = input("Enter the new name for the subject:\n>")
        if not subject_handler._check_subject(new_subject):
            subject_handler.edit_subject(existing_subject,new_subject)
        else:
            print(f"subject: '{new_subject}' already exists")
    else:
        print(f"subject: {existing_subject} doesn't exists")



def add_topics(topic_handler):
    """ Handles user input for adding topics to subjects."""
    while True:
        subject = input("Enter subject to add topics (or 'exit' to finish):\n> ")
        subject = str(map(str.strip(),subject))
        
        if subject.lower() == 'exit':
            break

        if topic_handler._get_subject_id(subject):
            topic_names = input(f"Enter topics for {subject} (comma-separated):\n> ").split(",")
            if not topic_handler._check_topic(topic_names):
                topic_names = [t.strip() for t in topic_names if t.strip()]
        
                if topic_names:
                    topic_handler.add_topic(subject, topic_names)
            else:
                print(f"topic: '{topic_names}' already exists")
                break
        else:
            print(f"subject: '{subject}' doesn't exist. ")


def edit_topic(topic_handler):
    """ Handles user input for editing a topic."""
    subject = input("Enter subject to rename its topic:\n> ").strip()
    if topic_handler._get_subject_id(subject): # To make things dynamic and notify the user instantly.

        old_topic = input("Enter the current topic name:\n> ").strip()
        if topic_handler._check_topic(old_topic):
            new_topic = input("Enter the new topic name:\n> ").strip()
            if subject and old_topic and new_topic:
                topic_handler.edit_topic(subject, old_topic, new_topic)
        else:
            print(f"topic: {old_topic} doesn't exist.")
    else:
        print(f"subject: {subject} doesn't exist.")



def delete_subject(subject_handler):
    """Handles user input for deleting a subject."""
    subject = input("Enter subject to delete:\n> ").strip()
    if subject:
        subject_handler.delete_subject(subject)

def delete_topic(topic_handler):
    """Handles user input for deleting a topic."""
    subject = input("Enter subject of the topic to delete:\n> ").strip()
    topic = input("Enter topic to delete:\n> ").strip()
    
    if subject and topic:
        topic_handler.delete_topic(subject, topic)

def main():
    """Main program loop."""
    initalize_database(db_path, schema_file)

    subject_handler = Subject(db_path)
    topic_handler = Topic(db_path)

    while True:
        print("\nOptions:")
        print("1. Add Subjects")
        print("2. Add Topics")
        print("3. Edit Subject")
        print("4. Edit Topic")
        print("5. Delete Subject")
        print("6. Delete Topic")
        print("7. Exit")

        choice = input("Choose an option:\n> ").strip()

        if choice == "1":
            add_subjects(subject_handler)
        elif choice == "2":
            add_topics(topic_handler)
        elif choice == "3":
            edit_subject(topic_handler)
        elif choice == "4":
            edit_topic(topic_handler)
        elif choice == "5":
            delete_subject(subject_handler)
        elif choice == "6":
            delete_topic(topic_handler)
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose again.")

