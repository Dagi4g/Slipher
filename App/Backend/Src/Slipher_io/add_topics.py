# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def add_topics_to_subject(topic_handler):
    """ Handles user input for adding topics to subjects."""
    while True:
        subject = input("Enter subject to add topics (or 'q' for quiting):\n> ")
        # i guess i should use a for loop with the map function.
        if subject.lower() == 'q':
            break
        add_topic(topic_handler,subject)

def add_topic(topic_handler,subject):

    if topic_handler._get_subject_id(subject):# this makes things dynamic. 
        topic_names = input(f"Enter topics for '{subject}' (comma-separated):\n> ").split(",")
        for topic in map(str.strip,topic_names):
            if not topic_handler._check_topic(topic):
                topic_handler.add_topic(subject, topic_names)
            else:
                print(f"topic: '{topic}' already exists")
    else:
        print(f"subject: '{subject}' doesn't exist. ")



