# Copyright 2025 Dagim                            #                                                 # Licensed under the Apache License, Version 2.0 (the "License");

"""Schedules the next day to review a topic."""

import sqlite3

from initentity import InitEntity


class scheduler(InitEntity):
    """A class for scheduling the next review day of a subject"""
    def calculate(self):
        

