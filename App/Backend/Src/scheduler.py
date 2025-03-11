# Copyright 2025 Dagim                            
#                                                 
# Licensed under the Apache License, Version 2.0 (the "License");


"""Schedules the next day to review a topic."""
import math
import sqlite3
from datetime import datetime ,timedelta,date

from initentity import InitEntity
import config


class Scheduler(InitEntity):
    """A class for scheduling the next review day of a subject"""
    def __init__(self,database: str):
        super().__init__(database)
        self.review_factor = 0.6
    def _get_review_day(self) -> list[tuple[int,str]]:
        
        """Returns a list that contain tuple of topic_id and next review day."""
        query = "SELECT topics.topic_id FROM topics WHERE NOT EXISTS (SELECT 1 FROM reviews_box WHERE reviews_box.topic_id = topics.topic_id)"# this query is only used to extract topic id's.
        unscheduled_topic_ids = self.connection.execute(query).fetchall()
        # for each unschdule id,schedule them.
        next_review_day = []
        for topic_id in unscheduled_topic_ids:
            next_review, box_level = self._calculate_next_review(topic_id,rating,last_seen)
            next_review_day.append(topic_id)

        return next_review_day

    def save_in_review_table(self) -> None:
        """Save the calculated value from _get_review_day to the database."""
        query = "INSERT INTO reviews_box(topic_id,box_level,next_review) VALUES(?,?,?)"

        topics = self._get_review_day()
        for topic_id,box_level,next_rievew in topics:
            self._execute(query,(topic_id,box_level,next_rievew))

    def _check_box(self) -> int:
        """check if a particular topic is found in a box."""
        n = 0
        for i in range(5):
            box_level = self.connection.execute("SELECT box_level FROM reviews_box WHERE box_level = ?",(n,))
            
            
            if len(box_level.fetchall()) > 0:
                
                return n # just one value is necessary.
            n += 1
    def _calculate_next_review(self,topic_id: int )-> list[str,int]:
        """ a class for only calculating the next review day.
        typical usage:
            review_day,box_level = self._calculate_next_review(topic_id , review_factor)
        """
        last_seen,rating = self.connection.execute("SELECT last_seen, rating FROM topics WHERE topic_id = ?",(topic_id,)).fetchall()[0]# indexing at the 0 position is necessary because execute returns a list of tuplewhich is unconfertable for unpacking. 
        last_seen = datetime.strptime(last_seen,'%Y-%m-%d')# change the string day into datetime object to make adding days easy.

        review_interval = round(math.e**(self.review_factor*int(rating)))

        next_review = timedelta(review_interval) # By using this function i can create a datetime object making easy to add and subtract days .
        next_review_date = last_seen + next_review
        box_level = review_interval//5
        
        return [next_review_date.strftime("%Y-%m-%d"),box_level]



    def _check_date(self) -> list[int]:
        """Check if the review day is today and return those list of topics that a will be reviewed today.""" 
        n = (self._check_box(),)
        review_date = self.connection.execute("SELECT reviews_box.topic_id, reviews_box.next_review FROM reviews_box WHERE box_level = ?",n).fetchall()
        topic_ids = []

        for topic_id,review_date in review_date:
            check_review = review_date == date.today().isoformat() # I wish i could better structure this part because I think using "=" sign might be confusing.
            if check_review :
                topic_ids.append(topic_id)
        return topic_ids                

    def show_review(self) -> None:
        """Print to the user the scheduled topic"""
        topic_ids = self._check_date()
        for topic_id in topic_ids: 
            topic = self.connection.execute("SELECT name FROM topics WHERE topic_id = ? ",(topic_id,)).fetchall()
            print(f"can you mention the fundumental principle of '{topic[0][0]}'?")
            respond = input(f"\nDo you want to study \"{topic[0][0]}\" press \"y\" or you remember it well \"q\" to quit:\n> ")
            if respond == "y":
                return
            else :
                last_seen = date.today().isoformat()
                self._execute("UPDATE topics SET last_seen = ? WHERE topic_id = ?",(last_seen,topic_id))
                





def run_schedule():
    """Runs the schedule class."""
    s = Scheduler(config.db_path)
    s.save_in_review_table()
    s._get_review_day()

    next_review,box_level = s._calculate_next_review(1)
    print(next_review,box_level)

if __name__ == "__main__":
    run_schedule()
