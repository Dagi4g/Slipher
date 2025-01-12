import sqlite3

con = sqlite3.Connection("test.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test (name ,first_appered )")


con.commit()
print("data base has created successfully")

data = ({"name" : "dagim","year" : "2004-17-9"},
        {"name" : "hana", "year" : "2004-25-8"}
        )

cur.executemany("INSERT INTO test VALUES(:name,:year)",data)

con.commit()
