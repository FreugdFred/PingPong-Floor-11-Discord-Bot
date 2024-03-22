from typing import List, Tuple

from database.match_queries import find_matches_by_discord_name
from utils.genric_helpers import who_won_match


def calculate_new_elo(player1_elo: int, player2_elo: int, player1_victory: str) -> int:
    """
    Calculates the new Elo rating for player 1 after a match.

    Args:
        player1_elo (int): Elo rating of player 1.
        player2_elo (int): Elo rating of player 2.
        player1_victory (str): Indicates if player 1 won ('victory'), lost ('defeat'), or it was a draw.

    Returns:
        int: The new Elo rating of player 1.
    """
    player1_match_points = round(player1_elo / 10)
    player2_match_points = round(player2_elo / 10)

    if player1_victory == "victory":
        player1_elo += player2_match_points
    elif player1_victory == "defeat":
        player1_elo -= player1_match_points
    else:
        match_points_diff = abs(player1_match_points - player2_match_points)
        player1_elo += match_points_diff if player2_match_points > player1_match_points else -match_points_diff

    return player1_elo


def calculate_elo_gain(player1_elo: int, player2_elo: int, player1_victory: str) -> int:
    """
    Calculates the Elo gain for player 1 after a match.

    Args:
        player1_elo (int): Elo rating of player 1.
        player2_elo (int): Elo rating of player 2.
        player1_victory (str): Indicates if player 1 won ('victory'), lost ('defeat'), or it was a draw.

    Returns:
        int: The Elo gain for player 1.
    """
    player1_match_points = round(player1_elo / 10)
    player2_match_points = round(player2_elo / 10)

    if player1_victory == "victory":
        return player2_match_points
    elif player1_victory == "defeat":
        return -player1_match_points
    else:
        match_points_diff = abs(player1_match_points - player2_match_points)
        return match_points_diff if player2_match_points > player1_match_points else -match_points_diff


def calculate_new_player_elo(discord_name: str) -> int:
    """
    Calculates the new Elo rating for a player based on their match history.

    Args:
        discord_name (str): The Discord name of the player.

    Returns:
        int: The new Elo rating of the player.
    """
    base_elo = 800
    all_player_matches = find_matches_by_discord_name(discord_name)
    elo_gain = sum(get_elo_gain_from_match(match, discord_name) for match in all_player_matches)
    return base_elo + elo_gain


def get_elo_gain_from_match(match: Tuple, discord_name: str) -> int:
    """
    Gets the Elo gain for a player from a match.

    Args:
        match (Tuple): A tuple containing match details.
        discord_name (str): The Discord name of the player.

    Returns:
        int: The Elo gain for the player from the match.
    """
    if discord_name == match[1]:
        return match[3]
    else:
        return match[6]


def calc_winrate(matches: List[Tuple], discord_name: str) -> float:
    """
    Calculates the win rate of a player based on their matches.

    Args:
        matches (List[Tuple]): A list of tuples containing match details.
        discord_name (str): The Discord name of the player.

    Returns:
        float: The win rate of the player.
    """
    won_matches = sum(1 for match in matches if who_won_match(match, discord_name))
    total_matches = len(matches)
    return (won_matches / total_matches) * 100 if total_matches > 0 else 0.0
