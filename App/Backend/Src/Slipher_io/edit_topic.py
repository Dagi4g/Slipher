# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def get_valid_subject(topic_handler)-> str:
    """Ask the user for existing subject.

    Args :
        subject_handler(class): is the class that manages database operations in subjects table.

    Return: 
        - None : if the subject doesn't exists.
        - str : the subject name."""
    while True:
        subject = input("please enter subject name to edit it's topic or \"q\" to quit: ")
        if subject.lower() == "q":
            return None

        if topic_handler._get_subject_id(subject):
            return subject
        else:
            print(f"{subject} doesn't exist.")
            choice = input(f"Do you want to retry (1), add '{subject}' (2) or quit(3)?: ")
            if choice == 1:#The user wants to retry.
                continue
 
            elif choice == 2:#The user wants to add the subject,so add it to the database.
                subject = subject.split(",")
                # The user maight add subject separeting it with comma.
                #the name of the subject must be processed before adding it to the database.
                subject_name = [s.strip() for s in subject if s.strip()]
                subject_handler.add_subject(subject_name)
                return
            elif choice == 3:#The user wants to quit
                return None


def get_valid_topic(topic_handler):
    while True:
        #ask the user until they give the right topic or quit.
        old_topic = input("enter the name of the topic to be edited or \"q\" to quit:\n> ")
        if old_topic.lower() == "q":
            return None
        if topic_handler._check_topic(old_topic):# the old topic exists so return it to edit.
            return old_topic
        else:
            return None

def edit_topic(topic_handler): 
    #by having both subject and topic handlers i can do multiple operations .

    # in the main module the topic handler is passes but right know i am passing subject_handler.
    while True:
        existing_subject = get_valid_subject(topic_handler)
        if existing_subject is None:
            print("operation cancelled.")
            # User wants to quit
            return # Exit
        # The subject users entered exists so,
        # Get the name of the old topic.
        existing_topic = get_valid_topic(topic_handler)
        if existing_topic is None:
            return
        new_topic = input("please enter the name of the new subject: ")
        topic_handler.edit_topic(existing_subject,existing_topic,new_topic)




