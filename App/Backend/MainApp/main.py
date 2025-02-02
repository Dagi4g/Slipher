# Copyright 2025 Dagim 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sqlite3
from datetime import date

from init_db_connection import InitEntity,initalize_database
from subject import Subject
from topic import Topic
from config import data_base_path, schema_file


# Right now i am not concerned about sql conjector attack but in future this will be fixed

# Eventhough i want to have some beautiful user interface ,creating the table for subject,topic and subtopic in the start will help me identify usefull approaches




# THE TEST PEOGRAM

def main() :
    initalize_database(data_base_path,schema_file)
    subject_names = input("please enter the subject\n> ").split(",")
    sub = Subject(data_base_path)
    sub.add_subject(subject_names)
    top = Topic(data_base_path)

    for subject in subject_names:
        # this current program works for adding one topic to one subject .
        # incase there are different subjects this code allows to add topics topics for each.

        topic_name = input(f"add topics to {subject}\n> ").split(",")
        print(subject)
        top.add_topic(subject,topic_name) # the subject must be a tuple in order to eliminate "sqlite3.programming error".

    # Test programm for edit class .
    
    # The next thing to do is to first chck for the subject first then check for topic and last not atleast check the existance of topic.
    """existing_subject = input("Enter the subject to edited it's topic: ")
    saved_topic = input("Enter the saved topic: ")
    new_topic = input("Enter the topic topic: ")

    top.edit_topic(existing_subject,saved_topic,new_topic)"""


    # Deleting existing subject.
    deleted = input("add delete subject: ")
    sub.delete_subject(deleted)






