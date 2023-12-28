import sqlite3 as sql
import os


class SqliteDbHelper:
    def __init__(self) -> None:
        """
        Purpose: 
        """
    # end default constructor

    @property
    def connect(self) -> sql.Connection:
        """
        Returns a connection to the SQLite database.

        :return: A connection object to the SQLite database.
        :rtype: sql.Connection
        """
        path: str = os.path.join(".", "data", "db", "isaretler.db")
        return sql.connect(path)
