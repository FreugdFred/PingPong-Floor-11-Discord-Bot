from database.player_queries import (
    find_player_by_discord_name,
    delete_user_by_discord_name,
    add_player,
)
from services.message_data import MessageData
from utils.decorators import admin_only
from utils.calc_elo import calculate_new_player_elo


def add_player_logic(message_data: MessageData) -> str:
    """
    Adds a player to the competition.

    Args:
        message_data (MessageData): The message data containing necessary information.

    Returns:
        str: Confirmation message indicating success or failure.
    """
    if find_player_by_discord_name(message_data.author):
        return "You are already in the competition!"

    if not message_data.just_message:
        return "You need to specify a player name!"

    new_elo_player = calculate_new_player_elo(message_data.author)

    if not add_player(
        message_data.just_message,
        message_data.author,
        message_data.guild,
        new_elo_player,
    ):
        return "Something went wrong, buddy"

    return f"{message_data.author} has added {message_data.just_message} to the competition!"


@admin_only
def delete_player(message_data: MessageData) -> str:
    """
    Deletes a player from the competition (admin-only).

    Args:
        message_data (MessageData): The message data containing necessary information.

    Returns:
        str: Confirmation message indicating success or failure.
    """
    if not find_player_by_discord_name(message_data.author):
        return "You are not in the competition, you can't be removed!"

    if not delete_user_by_discord_name(message_data.author):
        return "Something went wrong, buddy"

    return f"{message_data.author} has been removed from the competition!"


def display_help(message_data: MessageData) -> str:
    """
    Displays help information about the bot's commands.

    Args:
        message_data (MessageData): The message data containing necessary information.

    Returns:
        str: The help text.
    """
    help_text: str = """
This discord bot records matches from pingpong floor 11
It also records elo for every player

The commands:
!pingpong addme <Your nickname in the contest>
Example: !pingpong addme BigButterBoy
Adds you to the pingpong division of the 11 floor with a nickname of your liking

!pingpong removeme
Example: !pingpong removeme
removes you to the pingpong division of the 11 floor

!pingpong addmatch <points from you>-<points from your opponent> <your opponents discord name> 
Example: !pingpong addmatch 12-10 .shrekdeck
add a match with you and a opponent

!pingpong matches <discord name>
Example: !pingpong matches .shrekdeck
displays the matches from a given disord name

!pingpong ranks
Example: !pingpong ranks
displays the ranks of every player in the competition

!pingpong winrate <discord name>
Example: !pingpong winrate .shrekdeck
displays the winrate from a given discord name

Github code for this code: https://github.com/FreugdFred/PingPong-Floor-11-Discord-Bot
"""
    return help_text
