from database.player_queries import find_all_players_by_discord_channel, find_player_by_discord_name
from database.match_queries import find_matches_by_discord_name
from services.message_data import MessageData
from utils.format_queries import format_leaderboard
from utils.calc_elo import calc_winrate

def make_leaderboard(message_data: MessageData) -> str:
    """
    Generates a leaderboard for players in a specific Discord channel.

    Args:
        message_data (MessageData): The message data containing necessary information.

    Returns:
        str: The formatted leaderboard string.
    """
    all_players_from_specific_channel = find_all_players_by_discord_channel(
        message_data.guild
    )
    return format_leaderboard(all_players_from_specific_channel)

def make_winrate(message_data: MessageData) -> str:
    """
    Calculates and returns the winrate of a player.

    Args:
        message_data (MessageData): The message data containing necessary information.

    Returns:
        str: The winrate of the player.
    """
    player_name = message_data.just_message.lstrip()
    if not find_player_by_discord_name(player_name):
        return "This player does not exist"
    
    all_matches = find_matches_by_discord_name(player_name)
    if not all_matches:
        return f"No matches played, so no winrate"
    
    winrate = calc_winrate(all_matches, player_name)
    return f"The winrate of {player_name} is {round(winrate, 1)}%"
