from typing import List, Any

from utils.genric_helpers import sort_tuples_by_number

def format_find_all_matches(all_entries: List[Any]) -> str:
    """
    Formats a list of match entries into a readable string.

    Args:
        all_entries (List[Any]): A list of match entries, where each entry is a tuple containing match details.

    Returns:
        str: A formatted string containing information about all matches.
    """
    output_string = ""

    for entry in all_entries:
        # Determine the winner or if it's a draw
        won_name = entry[1] if int(entry[2]) > int(entry[5]) else entry[4]
        won_name = "draw" if int(entry[2]) == int(entry[5]) else won_name

        # Format match details
        output_string += f"match #{entry[0]} added by {entry[1]}: \n"
        output_string += f"    {entry[1]}: {entry[2]} points\n"
        output_string += f"    {entry[4]}: {entry[5]} points\n"
        output_string += f"    elo {entry[1]} gains: {entry[3]}\n"
        output_string += f"    elo {entry[4]} gains: {entry[6]}\n"
        output_string += f"    won: {won_name}\n"
        output_string += f"    date: {entry[7]}\n\n"

    return output_string


def format_leaderboard(all_entries: List[Any]) -> str:
    """
    Formats a list of player entries into a leaderboard string.

    Args:
        all_entries (List[Any]): A list of player entries, where each entry is a tuple containing player details.

    Returns:
        str: A formatted string containing the leaderboard information.
    """
    output_string: str = ""
    counter: int = 1

    # Sort the player entries by Elo rating
    for player in sort_tuples_by_number(all_entries):
        output_string += (
            f"{counter}. {player[0]}, Elo: {player[3]}, DiscordName: {player[1]}\n"
        )
        counter += 1

    return output_string
