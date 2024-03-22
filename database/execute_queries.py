import traceback
import sqlite3

from . import cursor, conn

from utils.genric_helpers import tuple_items_to_string


def execute_add_update_or_delete_query(query: str, parameters: tuple) -> bool:
    """
    Executes an add, update, or delete query on the database.

    Args:
        - query (str): The SQL query to be executed.
        - parameters (tuple): The parameters to be passed to the query.

    Returns:
        - bool: True if the execution is successful, False otherwise.
    """
    try:
        cursor.execute(query, tuple_items_to_string(parameters))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("Error executing add, update, or delete query:", traceback.format_exc())
        print(f"Query: {query}")
        print(f"Parameters: {parameters}")
        return False


def execute_fetch_query(
    query: str, parameters: tuple, fetch_one=False, fetch_all=False
) -> tuple:
    """
    Executes a fetch query on the database.

    Args:
        - query (str): The SQL query to be executed.
        - parameters (tuple): The parameters to be passed to the query.
        - fetch_one (bool): If True, fetches only one row. Default is False.
        - fetch_all (bool): If True, fetches all rows. Default is False.

    Returns:
        - tuple: A tuple containing the fetched results.
    """
    try:
        cursor.execute(query, tuple_items_to_string(parameters))
        if fetch_one:
            return cursor.fetchone()
        if fetch_all:
            return cursor.fetchall()
        else:
            raise sqlite3.Error("Did not specify fetch_one or fetch_all")
    except sqlite3.Error as e:
        print("Error executing fetch query:", traceback.format_exc())
        print(f"Query: {query}")
        print(f"Parameters: {parameters}")
        return tuple()
