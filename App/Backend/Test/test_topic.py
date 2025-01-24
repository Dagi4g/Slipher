import unittest
import sqlite3
from slifer import Topic,data_base

class testIfDataIsSaved(unittest.TestCase):

    def test_saved(self):
        topic = Topic(data_base)
        topic.add_topic(["mkwk"],["jjkrk"])
        con = sqlite3.connect(data_base)
        cur = con.cursor()
        extract = cur.execute("SELECT name FROM topics WHERE subject_id = (SELECT subject_id  FROM subjects WHERE name = 'dagim')")
        result = extract.fetchone()
        self.assertEqual(result,"jjkrk")

if __name__ == "__main__":
    unittest.main()


