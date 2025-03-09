# Copyright 2025 Dagim                            #                                                 # Licensed under the Apache License, Version 2.0 (the "License");

"""Schedules the next day to review a topic."""
import math
import sqlite3
from datetime import datetime ,timedelta,date

from initentity import InitEntity
import config


class Scheduler(InitEntity):
    """A class for scheduling the next review day of a subject"""
    def _get_review_day(self) -> list[tuple[int,str]]:
        """Returns a list that contain tuple of topic_id and next review day."""
        query = "SELECT topics.topic_id, topics.last_seen, topics.rating FROM topics WHERE NOT EXISTS (SELECT 1 FROM reviews_box WHERE reviews_box.topic_id = topics.topic_id)"
        # fetching from the data is tedious, creating an sql trigger is better because the only job of calculate is to calculate the next review.
        unscheduled_topics = self.connection.execute(query).fetchall()
        # for each unschdule id,schedule them.
        next_review_day = []
        for topic_id,last_seen , rating in unscheduled_topics:
            last_seen = datetime.strptime(last_seen,'%Y-%m-%d')# change the string day into datetime object to make adding days easy.

            review_interval = round(math.e**(0.6*int(rating)))

            next_review = timedelta(review_interval) # By using this function i can create a datetime object easly to add and subtract days .
            next_review_date = last_seen + next_review
            box_level = review_interval//5
            next_review_day.append((topic_id,box_level,next_review_date.strftime('%Y-%m-%d')))

        return next_review_day

    def save_in_review_table(self) -> None:
        """Save the calculated value from _get_review_day to the database."""
        query = "INSERT INTO reviews_box(topic_id,box_level,next_rievew) VALUES(?,?,?)"

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
    def _check_date(self) -> list[int]:
        """Check if the review day is today and return those list of topics that a will be reviewed today.""" 
        n = (self._check_box(),)
        review_date = self.connection.execute("SELECT reviews_box.topic_id, reviews_box.next_review FROM reviews_box WHERE box_level = ?",n).fetchall()
        print(review_date)
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
            print(f"can you mention the fundumental principle of {topic}?")
            respond = input("do you want to study \"{topic}\" press \"y\" or you remember it well \"q\" to quit")
            if respond == "y":
                return
            else :
                last_seen = date.today().isoformat()
                self.connection.execute("UPDATE topics SET last_seen = ? WHERE topic_id = ?",(last_seen,topic_id))





def run_schedule():
    """Runs the schedule class."
    s = Scheduler(config.db_path)
    s.show_review()

