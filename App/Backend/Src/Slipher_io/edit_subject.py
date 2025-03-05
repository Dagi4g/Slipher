# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

from .add_subjects import add_subjects

# I see myself having too much logic and really i need a creative way to structure this code.
# changing prompt each time wouldn't work so i should have to modularize each logic.
def edit_subject(subject_handler):
    """ Handles user input for editing subject."""
    while True: 
        # Keep asking until the user inputs a valide subject(existing) or cancels.
        existing_subject = input("Enter subject to rename:(\"q\" to quit)\n> ")
        if existing_subject.lower() == "q":
            break

        if subject_handler._check_subject(existing_subject): # The subject exists, So ask for new subject.
            while True:
                new_subject = input(f"Enter the new name for \"{existing_subject}\":\n>")
                if not subject_handler._check_subject(new_subject):
                    subject_handler.edit_subject(existing_subject,new_subject)
                    choice = input("Do you want to edit another subject(press enter) or quit(q): ")
                    if choice.lower() == "q":
                        prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                        break
                    else:
                        prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                        continue
                else:
                    print(f"subject: '{new_subject}' already exists")
                    choice = input("Do you want to add another name(press enter) or quit(q): ")
                    if choice.lower() == "q":
                        prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                        break
                    else:
                        prompt = "Please Enter subject name that doesn't exist:(\"q\" to quit)\n> " # Adabt the prompt.
                        continue
            else:
                print(f"subject: '{existing_subject}' doesn't exists")
                choice = input("Do you want to edit another subject(press enter) or quit(q): ")
                if choice.lower() == "q":
                    prompt = "Enter subject to rename:(\"q\" to quit)\n> " # Insure that the prompt is the original before quiting.
                    break
                else:
                    prompt =  "Please existing subject(\"q\" to quit):\n> "
                    continue

