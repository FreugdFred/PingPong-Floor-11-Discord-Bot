INSERT INTO Players (PlayerName, DiscordName, DiscordChannel, PlayerElo) VALUES ('NewPlayer', '.player', 'bot - bot', 1000);
INSERT INTO Players (PlayerName, DiscordName, DiscordChannel, PlayerElo) VALUES ('Jan', '.jan', 'bot - bot', 1234);
INSERT INTO Players (PlayerName, DiscordName, DiscordChannel, PlayerElo) VALUES ('bob', '.bob', 'bot - bot', 777);  


-- Inserting match data
INSERT INTO Matches (
    Player1Discord, Player1Points, Player1EloDifference,
    Player2Discord, Player2Points, Player2EloDifference,
    MatchDate, SubmittedBy, VerifiedBy, DiscordChannel
) VALUES (
    '.player', 100, 10, '.jan', 90, -10,
    '2024-02-21', 'Admin1', 'Admin2', 'bot - bot'
);

INSERT INTO Matches (
    Player1Discord, Player1Points, Player1EloDifference,
    Player2Discord, Player2Points, Player2EloDifference,
    MatchDate, SubmittedBy, VerifiedBy, DiscordChannel
) VALUES (
    '.bob', 120, 5, '.player', 110, -5,
    '2024-02-22', 'Admin2', 'Admin1', 'bot - bot'
);

-- Inserting more match data
INSERT INTO Matches (
    Player1Discord, Player1Points, Player1EloDifference,
    Player2Discord, Player2Points, Player2EloDifference,
    MatchDate, SubmittedBy, VerifiedBy, DiscordChannel
) VALUES (
    '.jan', 95, -5, '.bob', 98, -23,
    '2024-02-23', 'Admin1', 'Admin2', 'bot - bot'
);

INSERT INTO Matches (
    Player1Discord, Player1Points, Player1EloDifference,
    Player2Discord, Player2Points, Player2EloDifference,
    MatchDate, SubmittedBy, VerifiedBy, DiscordChannel
) VALUES (
    '.player', 110, 10, '.bob', 232, -28,
    '2024-02-24', 'Admin2', 'Admin1', 'bot - bot'
);

-- Inserting match data
INSERT INTO Matches (
    Player1Discord, Player1Points, Player1EloDifference,
    Player2Discord, Player2Points, Player2EloDifference,
    MatchDate, SubmittedBy, VerifiedBy, DiscordChannel
) VALUES (
    '.player', 100, 100, '.shrekdeck', 90, -100,
    '2024-02-23', 'Admin1', 'Admin2', 'bot - bot'
);