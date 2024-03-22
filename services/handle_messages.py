from services.logic.player_logic import add_player_logic, delete_player, display_help
from services.logic.match_logic import delete_match, find_matches, add_a_match
from services.logic.elo_logic import make_leaderboard, make_winrate
from services.command_names import CommandNames
from services.message_data import MessageData

def handle_messages(message) -> str:
    """
    Handles incoming messages and performs corresponding actions based on the command.

    Args:
        message (Any): The incoming message object.

    Returns:
        str: The response message.
    """
    command_names_obj = CommandNames(message.content)
    message_data = MessageData(
        str(message.author),
        str(message.guild),
        str(command_names_obj.main_command),
        str(command_names_obj.second_command),
        str(command_names_obj.message_without_command),
        str(command_names_obj.admins),
    )

    if command_names_obj.second_command == command_names_obj.addme_command:
        return add_player_logic(message_data)

    elif command_names_obj.second_command == command_names_obj.removeme_command:
        return delete_player(message_data)

    elif command_names_obj.second_command == command_names_obj.addmatch_command:
        return add_a_match(message_data)

    elif command_names_obj.second_command == command_names_obj.removematch_command:
        return delete_match(message_data)

    elif command_names_obj.second_command == command_names_obj.showmatches_command:
        return find_matches(message_data)

    elif command_names_obj.second_command == command_names_obj.showranks_command:
        return make_leaderboard(message_data)

    elif command_names_obj.second_command == command_names_obj.showwinrate_command:
        return make_winrate(message_data)

    elif command_names_obj.second_command == command_names_obj.help_command:
        return display_help(message_data)

    return "I don't understand that command."

