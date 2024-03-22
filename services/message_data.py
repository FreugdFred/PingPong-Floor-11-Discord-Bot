from dataclasses import dataclass
from typing import List

@dataclass
class MessageData:
    """
    Represents data associated with a Discord message.

    Attributes:
        author (str): The author of the message.
        guild (str): The guild (server) where the message was sent.
        first_command (str): The first part of the command in the message.
        second_command (str): The second part of the command in the message.
        just_message (str): The actual message content.
        admins (List[str]): A list of administrators for the bot.
    """
    author: str
    guild: str
    first_command: str
    second_command: str
    just_message: str
    admins: List[str]
