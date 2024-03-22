def sort_tuples_by_number(tuples: tuple) -> tuple:
    """
    Sorts a list of tuples based on the fourth element in descending order.

    Args:
        - tuples (tuple): A list of tuples.

    Returns:
        - tuple: The sorted list of tuples.
    """
    sorted_tuples: tuple = sorted(tuples, key=lambda x: x[3], reverse=True)
    return sorted_tuples


def match_outcome_to_string(player1_points: int, player2_points: int) -> str:
    """
    Determines the match outcome based on the points of two players.

    Args:
        - player1_points (int): Points scored by Player 1.
        - player2_points (int): Points scored by Player 2.

    Returns:
        - str: The match outcome - "victory", "defeat", or "draw".
    """
    if player1_points > player2_points:
        return "victory"
    elif player1_points < player2_points:
        return "defeat"
    else:
        return "draw"


def tuple_items_to_string(original_tuple: tuple) -> tuple:
    """
    Converts each element in a tuple to a string.

    Args:
        - original_tuple (tuple): The original tuple.

    Returns:
        - tuple: The tuple with all elements converted to strings.
    """
    return tuple(str(element) for element in original_tuple)

def who_won_match(match: tuple, name: str) -> bool:
    """
    Determines whether a player won a match based on the match details.

    Args:
        match (tuple): A tuple containing match details in the format (match_id, player1, score1, player2, score2).
        name (str): The name of the player whose victory is being checked.

    Returns:
        bool: True if the player won the match, False otherwise.
    """
    # Check if the player is player2 in the match and their score is higher than player1's score
    if match[1] == name:
        return match[2] > match[5]
    # Check if the player is player1 in the match and their score is lower than player2's score
    else:
        return match[2] < match[5]

