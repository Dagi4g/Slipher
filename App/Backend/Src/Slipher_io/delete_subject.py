# Copyright 2025 Dagim
#
# Licensed under the Apache License, Version 2.0 (the "License");

def delete_subject(subject_handler):
    """Handles user input for deleting a subject."""
    subject = input("Enter subject to delete:\n> ").strip()
    if subject:
        subject_handler.delete_subject(subject)
