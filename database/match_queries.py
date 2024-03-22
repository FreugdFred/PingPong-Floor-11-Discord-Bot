from .execute_queries import execute_add_update_or_delete_query, execute_fetch_query


def add_match(
    Player1_discord: str,
    player1_points: int,
    Player1_elo_difference: int,
    player2_discord: str,
    player2_points: int,
    Player2_elo_difference: int,
    match_date: str,
    submitted_by: str,
    verified_by: str,
    discord_channel: str,
) -> bool:
    """
    Adds a match to the database.

    Args:
        - Player1_discord (str): Discord name of Player 1.
        - player1_points (int): Points scored by Player 1.
        - Player1_elo_difference (int): Elo difference for Player 1.
        - player2_discord (str): Discord name of Player 2.
        - player2_points (int): Points scored by Player 2.
        - Player2_elo_difference (int): Elo difference for Player 2.
        - match_date (str): Date of the match.
        - submitted_by (str): Discord name of the person who submitted the match.
        - verified_by (str): Discord name of the person who verified the match.
        - discord_channel (str): Discord channel where the match was played.

    Returns:
        - bool: True if the addition is successful, False otherwise.
    """
    query = "INSERT INTO Matches (Player1Discord, Player1Points, Player1EloDifference, Player2Discord, Player2Points, Player2EloDifference, MatchDate, SubmittedBy, VerifiedBy, DiscordChannel) VALUES (?,?,?,?,?,?,?,?,?,?)"
    parameters = (
        Player1_discord,
        player1_points,
        Player1_elo_difference,
        player2_discord,
        player2_points,
        Player2_elo_difference,
        match_date,
        submitted_by,
        verified_by,
        discord_channel,
    )
    return execute_add_update_or_delete_query(query, parameters)


def delete_match_by_match_id(match_id: int) -> bool:
    """
    Deletes a match from the database based on the match ID.

    Args:
        - match_id (int): ID of the match to be deleted.

    Returns:
        - bool: True if the deletion is successful, False otherwise.
    """
    query = "DELETE FROM Matches WHERE MatchID = ?"
    parameters = (match_id,)
    return execute_add_update_or_delete_query(query, parameters)


def find_matches_by_discord_name(name: str) -> tuple:
    """
    Finds all matches involving a player by their Discord name.

    Args:
        - name (str): Discord name of the player.

    Returns:
        - tuple: A tuple containing the fetched results.
    """
    query = "SELECT * FROM Matches WHERE Player1Discord = ? OR Player2Discord = ?"
    parameters = (name, name)
    return execute_fetch_query(query, parameters, fetch_all=True)


def find_all_matches_by_discord_channel(discord_channel: str) -> tuple:
    """
    Finds all matches played in a specific Discord channel.

    Args:
        - discord_channel (str): Discord channel name.

    Returns:
        - tuple: A tuple containing the fetched results.
    """
    query = "SELECT * FROM Matches WHERE DiscordChannel =?"
    parameters = (discord_channel,)
    return execute_fetch_query(query, parameters, fetch_all=True)


def find_match_by_match_id(match_id: int) -> tuple:
    """
    Finds a match by its match ID.

    Args:
        - match_id (int): ID of the match to be fetched.

    Returns:
        - tuple: A tuple containing the fetched result.
    """
    query = "SELECT * FROM Matches WHERE MatchID =?"
    parameters = (match_id,)
    return execute_fetch_query(query, parameters, fetch_one=True)
