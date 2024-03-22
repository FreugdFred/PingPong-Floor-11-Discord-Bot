from .execute_queries import execute_add_update_or_delete_query, execute_fetch_query


def delete_user_by_discord_name(discord_name: str) -> bool:
    """
    Deletes a user from the database based on their Discord name.

    Args:
        - discord_name (str): Discord name of the user to be deleted.

    Returns:
        - bool: True if the deletion is successful, False otherwise.
    """
    query = "DELETE FROM Players WHERE DiscordName = ?"
    parameters = (discord_name,)
    return execute_add_update_or_delete_query(query, parameters)


def add_player(
    name: str, discord_name: str, discord_channel: str, player_elo: int = 800
) -> bool:
    """
    Adds a player to the database.

    Args:
        - name (str): Name of the player.
        - discord_name (str): Discord name of the player.
        - discord_channel (str): Discord channel name.

    Returns:
        - bool: True if the addition is successful, False otherwise.
    """
    query = "INSERT INTO Players (PlayerName, DiscordName, DiscordChannel, PlayerElo) VALUES (?, ?, ?, ?)"
    parameters = (name, discord_name, discord_channel, player_elo)
    return execute_add_update_or_delete_query(query, parameters)


def find_player_by_discord_name(discord_name: str) -> tuple:
    """
    Finds a player by their Discord name.

    Args:
        - discord_name (str): Discord name of the player.

    Returns:
        - tuple: A tuple containing the fetched result.
    """
    query = "SELECT * FROM Players WHERE DiscordName = ?"
    parameters = (discord_name,)
    return execute_fetch_query(query, parameters, fetch_one=True)


def find_all_players_by_discord_channel(discord_channel: str) -> tuple:
    """
    Finds all players in a specific Discord channel.

    Args:
        discord_channel (str): Discord channel name.

    Returns:
        tuple: A tuple containing the fetched results.
    """
    query = "SELECT * FROM Players WHERE DiscordChannel = ?"
    parameters = (discord_channel,)
    return execute_fetch_query(query, parameters, fetch_all=True)
