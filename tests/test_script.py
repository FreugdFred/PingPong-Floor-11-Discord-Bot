message = '!pingpong addmatch 97-22 .player'


class MessageData:
    author: str = '.shrekdeck'
    guild: str = 'bot - bot'
    first_command: str = '!pingpong'
    second_command: str = 'addmatch'
    just_message: str = '45-22 .hello'
    
    
message_data = MessageData()


def validate_add_match_syntax(message):
    split_message_list = message.split(' ')
    if len(split_message_list) != 2:
        return False
    
    match_points = split_message_list[0].split('-')
    if len(match_points) != 2:
        return False
    
    if not match_points[0].isdigit() or not match_points[1].isdigit():
        return False
    
    return True


print(validate_add_match_syntax(message_data.just_message))