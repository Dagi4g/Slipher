# Copyright 2025 Dagim                            #                                                 # Licensed under the Apache License, Version 2.0 (the "License");

"""Schedules the next day to review a topic."""
import math
import sqlite3

from initentity import InitEntity
import config


class Scheduler(InitEntity):
    """A class for scheduling the next review day of a subject"""
    def calculate(self):
       unscheduled_topics = self.connection.execute("SELECT topic_id FROM topics WHERE NOT EXISTS (SELECT 1 FROM reviews_box WHERE reviews_box.topic_id = topics.topic_id )").fetchall()
       # for each unschdule id,schedule them.
       for topic_id in unscheduled_topics:
           last_seen = self.connection.execute("SELECT last_seen FROM topics WHERE topic_id = ?",topic_id).fetchall()
           
           rating = self.connection.execute("SELECT rating FROM topics WHERE topic_id = ?",topic_id).fetchall()
           rating = int(rating[0][0])
           
           last_seen = last_seen[0][0].split("-")
           next_review = int(last_seen[-1]) + round(math.e**(0.6*rating))
           return next_review

s = Scheduler(config.db_path)
print(s.calculate())


