"""
The sqliteDbHelper module provides a class SqliteDbHelper that provides a property connect that returns a connection object to an SQLite database. 
The connect method constructs the path to the database file and then uses the sql.connect function to establish a connection.

@category: Data Access Layer, Helper
"""

import os
import sqlite3 as sql


class SqliteDbHelper:
    """The SqliteDbHelper class provides a property connect that returns a connection object to an SQLite database. 
    The connect method constructs the path to the database file and then uses the sql.connect function to establish a connection.

    @category: Data Access Layer, Helper
    """
    @property
    def connect(self) -> sql.Connection:
        """Returns a SQL connection object established by connecting to the database.

        Returns:
            sql.Connection: A SQL Connection object.
        """
        path: str = os.path.join(".", "data", "db", "isaretler.db")
        return sql.connect(path)
