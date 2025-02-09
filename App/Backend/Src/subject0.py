import sqlite3
from init_db_connection import InitEntity

class Subject(InitEntity):
    """Handles subject-related database operations."""

    def add_subject(self, subjects: list[str]) -> None:
        """Adds subjects if they don't exist."""
        self._execute_many("INSERT INTO subjects (name, rating) VALUES (?, ?)", 
                           [(s.strip(), 3) for s in subjects if not self._exists(s)], "Subjects added successfully.")

    def edit_subject(self, old: str, new: str) -> None:
        """Renames a subject if it exists and the new name is available."""
        self._execute("UPDATE subjects SET name = ? WHERE name = ?", (new, old),
                      f"'{old}' renamed to '{new}'." if self._exists(old) and not self._exists(new) 
                      else f"Cannot rename '{old}'.")

    def delete_subject(self, subject: str) -> None:
        """Deletes a subject if it exists."""
        self._execute("DELETE FROM subjects WHERE name = ?", (subject,),
                      f"'{subject}' deleted." if self._exists(subject) else f"'{subject}' doesn't exist.")

    def _exists(self, subject: str) -> bool:
        """Checks if a subject exists in the database."""
        return bool(self.cursor.execute("SELECT 1 FROM subjects WHERE name = ?", (subject,)).fetchone())

    def _execute(self, query: str, params: tuple, msg: str) -> None:
        """Helper method for single query execution with a message."""
        if msg.startswith("Cannot"):
            print(msg)
        else:
            self.cursor.execute(query, params)
            self.connection.commit()
            print(msg)

    def _execute_many(self, query: str, params: list[tuple], msg: str) -> None:
        """Helper method for batch execution with a message."""
        if params:
            self.cursor.executemany(query, params)
            self.connection.commit()
            print(msg)
        else:
            print("No new subjects added.")
