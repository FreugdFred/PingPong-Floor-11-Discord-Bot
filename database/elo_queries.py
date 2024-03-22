from .execute_queries import execute_add_update_or_delete_query, execute_fetch_query


def find_player_elo_by_discord_name(discord_name: str) -> tuple:
    """
    Finds the player's Elo by their Discord name.

    Args:
        - discord_name (str): The Discord name of the player.

    Returns:
        - tuple: A tuple containing the player's Elo.

    Raises:
        - Any exceptions raised by execute_fetch_query.
    """
    query = "SELECT PlayerElo FROM Players WHERE DiscordName = ?"
    parameters = (discord_name,)
    return execute_fetch_query(query, parameters, fetch_one=True)


def update_player_elo_by_discord_name(discord_name: str, new_elo: int) -> bool:
    """
    Updates the player's Elo by their Discord name.

    Args:
        - discord_name (str): The Discord name of the player.
        - new_elo (int): The new Elo value to be set.

    Returns:
        - bool: True if the update is successful, False otherwise.

    Raises:
        - Any exceptions raised by execute_add_update_or_delete_query.
    """
    query = "UPDATE Players SET PlayerElo = ? WHERE DiscordName = ?"
    parameters = (new_elo, discord_name)
    return execute_add_update_or_delete_query(query, parameters)
