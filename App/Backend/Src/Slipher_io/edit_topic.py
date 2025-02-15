# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def edit_topic(topic_handler):
    """ Handles user input for editing a topic."""
    subject = input("Enter subject to rename its topic:\n> ").strip()
    if topic_handler._get_subject_id(subject): # To make things dynamic and notify the user instantly.
        old_topic = input("Enter the current topic name:\n> ").strip()
        if topic_handler._check_topic(old_topic):
            new_topic = input("Enter the new topic name:\n>").strip()
            if subject and old_topic and new_topic:
                topic_handler.edit_topic(subjec, old_topic, new_topic)
        else:
            print(f"topic: '{old_topic}' doesn't exist.")
    else:
        print(f"subject: '{subject}' doesn't exist.")


