import json

'''
process_logs:
arguments:
1)input_file_name has all the event logs
2)output_file_name aggregate all user event data in a cleaner way
'''
def process_logs(input_file_name, output_file_name):
    # open the input file to parse log data
    input_file_obj = open(input_file_name)
    events_list = json.load(input_file_obj)
    input_file_obj.close()

    # create a dictionary to store user event data
    user_events = dict()

    for event in events_list:
        user_name = event["user"]
        command = event["command"]
        timestamp = event["timestamp"]
        if user_name not in user_events:
            user_events[user_name] = dict()
        if command not in user_events[user_name]:
            user_events[user_name][command] = list()
        user_events[user_name][command].append(timestamp)

    # dump all the user data in the output file
    output_file_object = open(output_file_name, "w")
    json.dump(user_events, output_file_object)
    output_file_object.close()


if __name__ == '__main__':
    process_logs("input.json", "output.json")
    #process_logs("input_1.json", "output_1.json")