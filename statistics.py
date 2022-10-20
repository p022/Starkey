import json

COMMANDS = {'red', 'blue', 'yellow', 'green'}


def get_most_used_command(user_events):
    command_count_dict = dict()
    for user, command_dict in user_events.items():
        for command in command_dict:
            # initialization
            if command not in command_count_dict:
                command_count_dict[command] = 0
            command_count_dict[command] += len(command_dict[command])
    result_command, max_command_count = None, 0
    for command, count in command_count_dict.items():
        if count > max_command_count:
            max_command_count = count
            result_command = command
    print("Command: {}, Usage Count: {}".format(result_command, max_command_count))


def get_user_with_most_commands(user_events):
    user_count_dict = dict()
    for user, command_dict in user_events.items():
        if user not in user_count_dict:
            # initialization
            user_count_dict[user] = 0
        for command in command_dict:
            user_count_dict[user] += len(command_dict[command])

    result_user, max_command_count = None, 0
    for user, count in user_count_dict.items():
        if count > max_command_count:
            max_command_count = count
            result_user = user
    print("User: {}, Commands Count: {}".format(result_user, max_command_count))


def get_commands_count_by_user(user_events):
    user = input("Enter the user:")
    if user not in user_events:
        print("User {} not found".format(user))
        return
    for command, timestamps in user_events[user].items():
        print("Command: {}, Usage Count: {}".format(command, len(timestamps)))


def get_most_used_command_by_user(user_events):
    user = input("Enter the user:")
    if user not in user_events:
        print("User {} not found".format(user))
        return

    result_command, max_command_count = None, 0

    for command, timestamps in user_events[user].items():
        if len(timestamps) > max_command_count:
            max_command_count = len(timestamps)
            result_command = command

    print("Command: {}, Usage Count: {}".format(result_command, max_command_count))
    return result_command, max_command_count


def get_most_active_user_by_command(user_events):
    command = input("Enter the command:")
    if command not in COMMANDS:
        print("Command {} not found. Commands can only be one of {}".format(command, COMMANDS))
    result_user, max_usage_count = None, 0
    for user, command_dict in user_events.items():
        if command in command_dict:
            if len(command_dict[command]) > max_usage_count:
                max_usage_count = len(command_dict[command])
                result_user = user
    print("User: {}, Usage Count: {}".format(result_user, max_usage_count))


def show_statistics(output_file_name):
    user_events = json.load(open(output_file_name))
    print("User Event Statistics")
    print("1. Get most used command")
    print("2. Get user with most commands")
    print("3. Get commands count by user")
    print("4. Get most used command by user")
    print("5. Get most active user by command")

    input_method_dict = {
        1: get_most_used_command,
        2: get_user_with_most_commands,
        3: get_commands_count_by_user,
        4: get_most_used_command_by_user,
        5: get_most_active_user_by_command
    }

    choice = int(input("Enter your choice:"))
    input_method_dict[choice](user_events)


if __name__ == '__main__':
    show_statistics("output.json")