# Copyright 2025 Dagim                            
#                                                 
# Licensed under the Apache License, Version 2.0 (the "License");


"""Schedules the next day to review a topic."""
from math import e
import sqlite3
from datetime import datetime ,timedelta,date

from initentity import InitEntity
import config


class Scheduler(InitEntity):
    """A class for scheduling the next review day of a subject"""
    def __init__(self,database: str):
        super().__init__(database)
        # in the future if i neede a value in this class.
    def _get_review_day(self) -> list[tuple[int,str]]:
        
        """Returns a list that contain tuple of topic_id and next review day."""
        query = "SELECT topics.topic_id FROM topics WHERE NOT EXISTS (SELECT 1 FROM reviews_box WHERE reviews_box.topic_id = topics.topic_id)"# this query is only used to extract topic id's.
        unscheduled_topic_ids = self.connection.execute(query).fetchall()
        # for each unschdule id,schedule them.
        next_review_day = []
        for topic_id in unscheduled_topic_ids:
            next_review, box_level = self._calculate_next_review(topic_id)
            next_review_day.append([topic_id,box_level,next_review])

        return next_review_day

    def save_in_review_table(self) -> None:
        """Save the calculated value from _get_review_day to the database."""
        query = "INSERT INTO reviews_box(topic_id,box_level,next_review) VALUES(?,?,?)"

        topics = self._get_review_day()
        for topic_id,box_level,next_review in topics:
            self._executemany(query,(topic_id,box_level,next_review,)) # Add topic data to review_box table in the database.


    def _check_box(self) -> int:
        """check if a particular topic is found in a box."""
        n = 0
        for i in range(5):
            box_level = self.connection.execute("SELECT box_level FROM reviews_box WHERE box_level = ?",(n,))
            
            
            if len(box_level.fetchall()) > 0:
                
                return n # just one value is necessary.
            n += 1
    def _calculate_next_review(self,topic_id: int,
                               review_factor = 0.6)-> list[str,int]:
        """ a class for only calculating the next review day and box level.
        typical usage:
            review_day,box_level = self._calculate_next_review(topic_id , review_factor)
            
            # the topic_id must be a tuple.
            
        returns:
            list of next review day and box level."""
        last_seen,rating = self.connection.execute("SELECT last_seen, rating FROM topics WHERE topic_id = ?",topic_id).fetchall()[0]# indexing at the 0 position is necessary because execute returns a list of tuplewhich is unconfertable for unpacking. 
        last_seen = datetime.strptime(last_seen,'%Y-%m-%d')# change the string day into datetime object to make adding days easy.

        review_interval = round(e**(review_factor*int(rating)))

        next_review = timedelta(review_interval) # By using this function i can create a datetime object making easy to add and subtract days .
        next_review_date = last_seen + next_review # while adding two days i encountered a bug saying that i can't add dates out of range.
        box_level = review_interval//5
        
        
        return [next_review_date.strftime("%Y-%m-%d"),box_level]



    def _check_date(self) -> list[int]:
        """Check if the review day is today and return those list of topics that a will be reviewed today.""" 
        # I feel like checking the box number is unessary as well as I should rewrite the logic.
        box_level = (self._check_box(),)
        review_date = self.connection.execute("SELECT reviews_box.topic_id, reviews_box.next_review FROM reviews_box WHERE box_level = ?",box_level).fetchall()
        topic_ids = []

        for topic_id,review_date in review_date:
            check_review = review_date == date.today().isoformat() # I wish i could better structure this part because I think using "==" sign might be confusing.
            if check_review :
                topic_ids.append(topic_id)
        return topic_ids                

    def show_review(self) -> None:
        #i will refactor this method into Slipher_io package.
        """Print to the user the scheduled topic"""
        topic_ids = self._check_date()
        for topic_id in topic_ids: 
            
            topic_name, rating = self.connection.execute("SELECT name,rating FROM topics WHERE topic_id = ? ",(topic_id,)).fetchone()
            print(f"can you mention the fundumental principle of '{topic_name}'?")
            respond = input(f"\npress \"y\" if you remembered it well, \"n\" if you don't.\n >")
            last_seen = date.today().isoformat()
            review_factor = 0.6
            if respond.lower() == "y":
                review_factor = min(1.5, review_factor+ 0.15)# the user rememered well so gradually increase the review factor.
                #from know on i thing review factor should be saved in the database and updated from that to not running into the same number again and again which is 0.7.
                rating += 0.3
                
            elif respond.lower()== "n" :
                review_factor = max(0.3,review_factor-0.1)
                rating -= 0.3
            
            self._execute("UPDATE topics SET last_seen = ?,rating = ?  WHERE topic_id = ?",(last_seen,rating,topic_id))
            print(review_factor)
            print(topic_id)

            next_review,box_level = self._calculate_next_review((topic_id,),review_factor)

            self._executemany("UPDATE reviews_box SET next_review = ? , box_level = ? WHERE topic_id = ?",[(next_review, box_level, topic_id)])
                





def run_schedule():
    """Runs the schedule class."""
    s = Scheduler(config.db_path)
    s.save_in_review_table()
    s._get_review_day()
    s.show_review()

if __name__ == "__main__":
    run_schedule()
