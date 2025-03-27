# Copyright 2025 Dagim                      #                                           # Licensed under the Apache License, Version 2.0 (the "License");                                                                   
# every method of this class can be used anywhere once it is initalized to a database.

import sqlite3
from datetime import date

from initentity import InitEntity
from config import db_path

class SubTopic(InitEntity):
    def add_subtopic(self,
                     topic_name: str,
                     subtopic_name: list[str],
                     last_seen : str = date.today().isoformat(),
                     ratings : int = 3
                     )-> None:
        self._get_topic_id(topic_name)
        formated_data = [
                {"topic_id":self.topic_id,
                 "subtopic_name": subtopic,
                 "last_seen" : last_seen,
                 "ratings" : ratings
                 } for subtopic in subtopic_name
                ]
        try:
            # this execute many will be refactored latter.
            self.cursor.executemany("INSERT INTO subtopics(topic_id,name,last_seen,ratings) VALUES (:topic_id,:subtopic_name,:last_seen,:ratings)",formated_data)
        except sqlite3.IntegrityError:
            print("subtopic: {subtopic_name exists")
        self.connection.commit()

    

    def _get_topic_id(self,topic_name):
        self.topic_id = 0
        extract = self.connection.execute("SELECT topic_id FROM topics WHERE name = ?",(topic_name,))
        result = extract.fetchone()
        if result:
            self.topic_id = result[0]
            return True
        else:
            return False

    #most of the work will be done in slipher.io
    def edit_subtopic(self,
                      topic_name: str,
                      old_subtopic_name : str,
                      new_subtopic_name: str):
        if self._get_topic_id(topic_name):# the topic exists.
            if self._check_subtopic(old_subtopic_name):
                self._execute("UPDATE subtopics SET name = ? WHERE name = ? and topic_id = ?",(new_subtopic_name,old_subtopic_name,self.topic_id))
                print(f"{old_subtopic_name} successfully change to {new_subtopic_name}")
            else:
                print(f"there is not subtopic named: {old_subtopic_name}")
        else:
            print(f"there is no topic named: {topic_name}")
                


    def _check_subtopic(self,subtopic):
        check = self.cursor.execute("SELECT 1 FROM subtopics WHERE name = ? AND topic_id = ?",(subtopic,self.topic_id)).fetchone()
        #i don't need to use _get_topic_id because the topic must be checked befor the subtopic.
        if check:#subtopic exists.
            return True
        else:
            return False



if __name__=="__main__":
    
    sub = SubTopic(db_path)
    sub.add_subtopic("topic1",["active transport ", "passive transport"])
    sub.edit_subtopic("topic1","passive transport","subtopic1")





