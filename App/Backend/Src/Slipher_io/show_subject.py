# Copyright 2025 Dagim                            #                                                 # Licensed under the Apache License, Version 2.0 (the "License");
"""Show all the subjects to the user"""

def show_subject(subject_handler):
    while True:
        subject_handler.show_subject()
        response = input("press enter to get to the  first page:\n>")
        return
