
import sqlite3
import csv

def sqlite_to_csv(database_path, table_name, csv_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    try:
        cursor.execute(f"select * from {table_name}")
        rows = cursor.fetchall()

        with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([description[0] for description in cursor.description])  # Write header
            writer.writerows(rows)

        print(f"Table '{table_name}' exported to '{csv_path}'")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()

def backup_all_tables(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        csv_path = f"{table_name}.csv"
        sqlite_to_csv(database_path, table_name, csv_path)

    conn.close()
    
if __name__ == "__main__":
    db = "slipher.db"
    backup_all_tables(db)


