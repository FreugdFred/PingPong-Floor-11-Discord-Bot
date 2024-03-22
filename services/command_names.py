from typing import List



class CommandNames:
    """
    Represents the command names parsed from a message content.

    Attributes:
        message_content (str): The content of the message.
        second_command (str): The second part of the command in the message.
        message_without_command (str): The message content without the command part.
        main_command (str): The main command string.
        addme_command (str): The command string for adding a player.
        removeme_command (str): The command string for removing a player.
        addmatch_command (str): The command string for adding a match.
        removematch_command (str): The command string for removing a match.
        showmatches_command (str): The command string for displaying matches.
        showranks_command (str): The command string for displaying ranks.
        showwinrate_command (str): The command string for displaying win rates.
        help_command (str): The command string for displaying help.
        admins (List[str]): A list of administrators for the bot.
    """

    def __init__(self, message_content: str = "") -> None:
        """
        Initializes the CommandNames object.

        Args:
            message_content (str, optional): The content of the message. Defaults to "".
        """
        self.message_content: str = message_content
        self.second_command: str = self.get_second_command()
        self.message_without_command: str = self.get_message_without_command()

        self.main_command: str = "!pingpong"
        self.addme_command: str = "addme"
        self.removeme_command: str = "removeme"
        self.addmatch_command: str = "addmatch"
        self.removematch_command: str = "removematch"
        self.showmatches_command: str = "matches"
        self.showranks_command: str = "ranks"
        self.showwinrate_command: str = "winrate"
        self.help_command: str = "help"

        self.admins: List[str] = [".shrekdeck"]

    def get_second_command(self) -> str:
        """
        Extracts the second command from the message content.

        Returns:
            str: The second command string.
        """
        try:
            return self.message_content.split(" ")[0]
        except IndexError:
            return ""

    def get_message_without_command(self) -> str:
        """
        Extracts the message content without the command part.

        Returns:
            str: The message content without the command part.
        """
        return self.message_content.replace(self.second_command, "").lstrip()
