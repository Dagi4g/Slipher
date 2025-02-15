# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def add_topics(topic_handler):
    """ Handles user input for adding topics to subjects."""
    while True:
        subject = input("Enter subject to add topics (or 'exit' to finish):\n> ")
        old_subject = str(map(str.strip(),subject))
        if subject.lower() == 'exit':
            break
        if topic_handler._get_subject_id(subject):# this makes things dynamic. 
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

