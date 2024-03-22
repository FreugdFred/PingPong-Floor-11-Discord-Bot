from database.match_queries import (
    delete_match_by_match_id,
    find_match_by_match_id,
    find_matches_by_discord_name,
    add_match,
)
from database.player_queries import find_player_by_discord_name
from database.elo_queries import (
    update_player_elo_by_discord_name,
    find_player_elo_by_discord_name,
)

from utils.decorators import admin_only
from utils.format_queries import format_find_all_matches
from utils.calc_elo import calculate_elo_gain, calculate_new_elo
from utils.genric_helpers import match_outcome_to_string

from services.message_data import MessageData

from typing import Tuple

import datetime

# import pprint


def add_a_match(message_data: MessageData) -> str:
    """
    Adds a match to the competition and updates players' Elo ratings.

    Args:
        message_data (MessageData): Message data containing match information.

    Returns:
        str: Confirmation message.
    """
    if not validate_add_match_text_syntax(message_data.just_message):
        return "Not the correct syntax, for questions send !pingpong help"

    player_two_name = message_data.just_message.split(" ")[1]
    validate_answer = validate_players(message_data.author, player_two_name)
    if validate_answer:
        return validate_answer

    (
        player_one_elo,
        player_two_elo,
        player_one_match_outcome,
        player_two_match_outcome,
        add_match_result,
    ) = make_add_match(
        message_data.just_message.split(" ")[0],
        message_data.author,
        player_two_name,
        message_data.guild,
    )
    if not add_match_result:
        return "Something went wrong buddy"

    result_player_one, result_player_two = update_players_elo(
        message_data.author,
        player_two_name,
        player_one_elo,
        player_two_elo,
        player_one_match_outcome,
        player_two_match_outcome,
    )
    if not result_player_one or not result_player_two:
        return "Something went wrong buddy"

    return f"{message_data.author} has added a match to {player_two_name}"


def update_players_elo(
    author_one: str,
    author_two: str,
    player_one_elo: int,
    player_two_elo: int,
    player_one_match_outcome: str,
    player_two_match_outcome: str,
) -> Tuple[str, str]:
    """
    Updates players' Elo ratings based on match outcome.

    Args:
        author_one (str): Name of the first player.
        author_two (str): Name of the second player.
        player_one_elo (int): Elo rating of the first player.
        player_two_elo (int): Elo rating of the second player.
        player_one_match_outcome (str): Outcome of the match for the first player.
        player_two_match_outcome (str): Outcome of the match for the second player.

    Returns:
        Tuple[str, str]: Results of updating Elo ratings for both players.
    """
    new_elo_player_one = calculate_new_elo(
        player_one_elo, player_two_elo, player_one_match_outcome
    )
    new_elo_player_two = calculate_new_elo(
        player_two_elo, player_one_elo, player_two_match_outcome
    )

    result_one = update_player_elo_by_discord_name(author_one, new_elo_player_one)
    result_two = update_player_elo_by_discord_name(author_two, new_elo_player_two)

    return result_one, result_two


def make_add_match(
    match_points: str, author_one: str, author_two: str, discord_channel: str
) -> Tuple[int, int, str, str, str]:
    """
    Creates a match and calculates Elo rating changes.

    Args:
        match_points (str): Points scored by each player in the match.
        author_one (str): Name of the first player.
        author_two (str): Name of the second player.
        discord_channel (str): Discord channel where the match occurred.

    Returns:
        Tuple[int, int, str, str, str]: Elo ratings, match outcomes, and match result.
    """
    player_one_elo = int(find_player_elo_by_discord_name(author_one)[0])
    player_two_elo = int(find_player_elo_by_discord_name(author_two)[0])

    player_one_points = int(match_points.split("-")[0])
    player_two_points = int(match_points.split("-")[1])

    player_one_match_outcome = match_outcome_to_string(
        player_one_points, player_two_points
    )
    player_two_match_outcome = match_outcome_to_string(
        player_two_points, player_one_points
    )

    player_one_elo_gain = int(
        calculate_elo_gain(player_one_elo, player_two_elo, player_one_match_outcome)
    )
    player_two_elo_gain = int(
        calculate_elo_gain(player_two_elo, player_one_elo, player_two_match_outcome)
    )

    result = add_match(
        author_one,
        player_one_points,
        player_one_elo_gain,
        author_two,
        player_two_points,
        player_two_elo_gain,
        datetime.datetime.now().strftime("%Y-%m-%d"),
        author_one,
        author_one,
        discord_channel,
    )

    return (
        player_one_elo,
        player_two_elo,
        player_one_match_outcome,
        player_two_match_outcome,
        result,
    )


def validate_add_match_text_syntax(message: str) -> bool:
    """
    Validates the syntax of the match message.

    Args:
        message (str): Match message.

    Returns:
        bool: True if syntax is valid, False otherwise.
    """
    split_message_list = message.split(" ")
    if len(split_message_list) != 2:
        return False

    match_points = split_message_list[0].split("-")
    if len(match_points) != 2:
        return False

    if not match_points[0].isdigit() or not match_points[1].isdigit():
        return False

    return True


def validate_players(author: str, author_two: str) -> str:
    """
    Validates the existence of players in the competition.

    Args:
        author (str): Name of the first player.
        author_two (str): Name of the second player.

    Returns:
        str: Error message if validation fails, empty string otherwise.
    """
    if not find_player_by_discord_name(author):
        return "You are not in the competition, you can't add a match!"

    if not find_player_by_discord_name(author_two):
        return "Your opponent doesn't exist, stop making up stuff buddy"

    return ""


@admin_only
def delete_match(message_data: MessageData) -> str:
    """
    Deletes a match from the database (admin-only).

    Args:
        message_data (MessageData): The message data containing necessary information.

    Returns:
        str: Confirmation message indicating success or failure.
    """
    try:
        match_id = int(message_data.just_message)
    except ValueError:
        return f"You did not put in the correct format, please try again. The format should be like this: {message_data.first_command} {message_data.second_command} 1"

    match = find_match_by_match_id(match_id)
    if not find_match_by_match_id(match_id):
        return "There is no match with that ID!"

    if not delete_match_by_match_id(match_id):
        return "Something went wrong, buddy"

    if not handle_reset_player_elo(match):
        return "Something went wrong, buddy"

    return f"The match with ID {match_id} has been deleted!"


def find_matches(message_data: MessageData) -> str:
    """
    Finds matches for a given Discord user.

    Args:
        message_data (MessageData): The message data containing necessary information.

    Returns:
        str: The formatted string containing match information.
    """
    if not message_data.just_message:
        return "You need to specify a player name!"

    if not find_player_by_discord_name(message_data.just_message):
        return f"{message_data.just_message} is not in the competition, you can't find matches by that discord name!"

    all_matches = find_matches_by_discord_name(message_data.just_message)
    if not (all_matches):
        return f"{message_data.just_message} has no matches played yet!"

    return format_find_all_matches(all_matches)


def handle_reset_player_elo(match: tuple) -> bool:
    """
    Resets player's Elo ratings after deleting a match.

    Args:
        match (tuple): The match details.

    Returns:
        bool: True if the process is successful, False otherwise.
    """
    player_one_disord, player_two_disord = match[1], match[4]
    player_one_match_elo_gains, player_two_match_elo_gains = match[3], match[6]
    try:
        player_one_current_elo = int(
            find_player_elo_by_discord_name(player_one_disord)[0]
        )
        player_two_current_elo = int(
            find_player_elo_by_discord_name(player_two_disord)[0]
        )
    except IndexError:
        return False

    query_one_success = update_player_elo_by_discord_name(
        player_one_disord, player_one_current_elo + player_one_match_elo_gains
    )
    query_two_success = update_player_elo_by_discord_name(
        player_two_disord, player_two_current_elo + player_two_match_elo_gains
    )

    return query_one_success and query_two_success
