# Copyright 2025 Dagim                            #                                                 # Licensed under the Apache License, Version 2.0 (the "License");

"""Schedules the next day to review a topic."""
import math
import sqlite3
from datetime import datetime ,timedelta

from initentity import InitEntity
import config


class Scheduler(InitEntity):
    """A class for scheduling the next review day of a subject"""
    def calculate(self) -> list[tuple[int,str]]:
        """Returns a list that contain tuple of topic_id and next review day."""
        query = "SELECT topics.topic_id, topics.last_seen, topics.rating FROM topics WHERE NOT EXISTS (SELECT 1 FROM reviews_box WHERE reviews_box.topic_id = topics.topic_id)"
        unscheduled_topics = self.connection.execute(query).fetchall()
        # for each unschdule id,schedule them.
        next_review_day = []
        for topic_id,last_seen , rating in unscheduled_topics:
            last_seen = datetime.strptime(last_seen,'%Y-%m-%d')# change the string day into datetime object

            review_interval = round(math.e**(0.6*int(rating)))

            next_review = timedelta(round(math.e**(0.6*rating)))
            next_review_date = last_seen + next_review
            next_review_day.append((topic_id,next_review_date.strftime('%Y-%m-%d')))

            return next_review_day

s = Scheduler(config.db_path)
print(s.calculate())


