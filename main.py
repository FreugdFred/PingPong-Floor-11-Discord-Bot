import discord

# Importing necessary modules
from services.command_names import CommandNames
from services.handle_messages import handle_messages
from utils.get_env import get_api_key

# Defining the main command from CommandNames class
main_command = CommandNames().main_command

# Getting the Discord bot token from environment variables
TOKEN = get_api_key()


async def send_message(message):
    """
    Asynchronously sends a message to the Discord channel.

    Args:
        message: The message object received from Discord.
    """
    try:
        # Handling messages and sending response
        response = handle_messages(message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    """
    Runs the Discord bot.
    """
    # Setting up intents to receive message content
    intents = discord.Intents.default()
    intents.message_content = True

    # Creating a Discord client instance
    client = discord.Client(intents=intents)

    # Event handler for bot ready status
    @client.event
    async def on_ready():
        """
        Event handler for bot being ready.
        """
        print(f"{client.user} is now running!")

    # Event handler for receiving messages
    @client.event
    async def on_message(message):
        """
        Event handler for receiving messages.
        Args:
            message: The message object received from Discord.
        """
        # Ignore messages from the bot itself
        if message.author == client.user:
            return

        # Check if the received message starts with the main command
        if message.content.split(" ")[0] != main_command:
            return

        # Extracting the command content
        message.content = message.content.replace(main_command + " ", "")

        # Sending the message for processing
        await send_message(message)

    # Running the Discord bot with the provided token
    client.run(TOKEN)


if __name__ == "__main__":
    # Entry point of the script
    run_discord_bot()
