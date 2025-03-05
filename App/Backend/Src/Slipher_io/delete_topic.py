# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def delete_topic(topic_handler):
    """Handles user input for deleting a topic."""
    subject_name = input("Enter subject of the topic to delete:\n> ").split(",")
    for subject in map(str.strip,subject_name):
        if topic_handler._get_subject_id(subject):
            # The subject already exists so continue deleting the topics.
            topic_name = input("Enter topic to delete:\n> ").split(",")
            for topic in map(str.strip,topic_name):
                topic_handler.delete_topic(subject, topic) 
        else:
            print(f"{subject} doesn't exists")
