# PingPong Floor 11 Discord Bot

This Discord bot is designed to manage pingpong matches and track Elo ratings for players participating in the competition held at Floor 11. Players can register, record matches, view their match history, check their Elo rankings, and analyze their win rates using various commands.

## Installation

To use the PingPong Floor 11 Discord Bot, follow these steps:

1. Clone the repository or download the source code.
2. Install the necessary dependencies.
3. Set up a Discord bot account and obtain the bot token.
4. Configure the bot token and at it to a file named .env, the token variable should be called TOKEN.
5. Deploy the bot to your preferred hosting platform or run it locally.

## Usage

### Commands

The bot responds to the following commands:

- `!pingpong addme <Your nickname in the contest>`: Adds the user to the pingpong division of the 11th floor with a chosen nickname.
  - Example: `!pingpong addme BigButterBoy`

- `!pingpong removeme`: Removes the user from the pingpong division of the 11th floor.
  - Example: `!pingpong removeme`

- `!pingpong addmatch <points from you>-<points from your opponent> <opponent's discord name>`: Records a match between the user and an opponent, along with the match score.
  - Example: `!pingpong addmatch 12-10 .butterBoy`

- `!pingpong matches <discord name>`: Displays the match history of the specified Discord user.
  - Example: `!pingpong matches .butterBoy`

- `!pingpong ranks`: Displays the Elo rankings of all players in the competition.

- `!pingpong winrate <discord name>`: Displays the win rate of the specified Discord user.

### Permissions

Make sure the bot has the necessary permissions to read and send messages in the channels where the commands are executed.

## Contributors

- [FreugdFred](https://github.com/FreugdFred)

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This Discord bot is provided as-is without any warranty. Use it at your own risk.