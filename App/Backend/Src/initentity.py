# Copyright 2025 Dagim                  
#
# Licensed under the Apache License, Version 2.0 (the "License");
"""Initalize database connection for other classes.

This class is meant to be inhereted buy other classes.

Usage :
    from initentity import InitEntity

    class ClassName(InitEntity):
        ...

"""

import os
import sys
import sqlite3

class InitEntity:
    """ A class that will be used to initalize the subject and topic class.

    typical usage:

        class ClassName(InitEntity):
            
            ...
    """
    def __init__(self, data_base: str) -> None:
        """ The database must be intialized first because it will be used later repetidly in the class. """
        # This try statment is used to privent injection attack.
        if not os.path.exists(data_base):
            print(f" Database: '{data_base}'  not found.")
            sys.exit()

        self.data_base = data_base
        try:
            self.connection = sqlite3.connect(data_base)
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT 1")
        except sqlite3.Error as e:
            print(f"Database Connection error:{e}")
            self.connection = None
        
    def _execute(self,script: str,value: str) -> None:
        """ Just for simple data insertion and deletion operations,
        this method cannot work for fetching data because it returns None type."""
        self.cursor.execute(script,value)
        self.connection.commit()

    def _executemany(self,script: str,values:tuple[str,str,str]):
        self.connection.executemany(script,values)
        self.connection.commit()# for adding a lotof values.

    def close(self)-> None:
        self.connection.close()
