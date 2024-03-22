import sqlite3


class DatabaseCreationError(Exception):
    """Custom exception for database creation errors."""


def create_database(database_name: str) -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Create a SQLite database and return a connection and cursor.

    Parameters:
    - database_name (str): The name of the SQLite database.

    Returns:
    - tuple[sqlite3.Connection, sqlite3.Cursor]: A tuple containing the SQLite connection and cursor.
    """

    try:
        conn: sqlite3.Connection = sqlite3.connect(database_name)
        cursor: sqlite3.Cursor = conn.cursor()

        create_player_table(cursor, conn)
        create_record_table(cursor, conn)

    except sqlite3.Error as e:
        print(str(e))
        raise DatabaseCreationError("Error creating the database.")

    return conn, cursor


def execute_query(query: str, cursor: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Execute a query on the SQLite database.

    Parameters:
    - query (str): The SQL query to be executed.
    - cursor (sqlite3.Cursor): The SQLite cursor.
    - conn (sqlite3.Connection): The SQLite connection.

    Returns:
    - None
    """
    try:
        cursor.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")


def create_player_table(cursor: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Create the Players table in the SQLite database.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor.
    - conn (sqlite3.Connection): The SQLite connection.

    Returns:
    - None
    """
    query = """
                CREATE TABLE IF NOT EXISTS Players (
                    PlayerName VARCHAR(50) NOT NULL,
                    DiscordName VARCHAR(50) NOT NULL,
                    DiscordChannel VARCHAR(100) NOT NULL,
                    PlayerElo INT DEFAULT 800,
                    PRIMARY KEY (PlayerName, DiscordName)
                );
            """
    execute_query(query, cursor, conn)


def create_record_table(cursor: sqlite3.Cursor, conn: sqlite3.Connection) -> None:
    """
    Create the Matches table in the SQLite database.

    Parameters:
    - cursor (sqlite3.Cursor): The SQLite cursor.
    - conn (sqlite3.Connection): The SQLite connection.

    Returns:
    - None
    """
    query = """
            CREATE TABLE IF NOT EXISTS Matches (
                MatchID INTEGER PRIMARY KEY AUTOINCREMENT,
                Player1Discord VARCHAR(50) NOT NULL,
                Player1Points INT NOT NULL,
                Player1EloDifference INT NOT NULL,
                Player2Discord VARCHAR(50) NOT NULL,
                Player2Points INT NOT NULL,
                Player2EloDifference INT NOT NULL,
                MatchDate DATE NOT NULL,
                SubmittedBy VARCHAR(50) NOT NULL,
                VerifiedBy VARCHAR(50) NOT NULL,
                DiscordChannel VARCHAR(100) NOT NULL,
                FOREIGN KEY (Player1Discord) REFERENCES Players(PlayerName),
                FOREIGN KEY (Player2Discord) REFERENCES Players(PlayerName)
            );
        """
    execute_query(query, cursor, conn)


conn, cursor = create_database("records.db")
