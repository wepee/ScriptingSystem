import requests
import logging
import json

with open('./config.json', 'r') as file:
    data = json.load(file)

message = {"tasks": [" Progress             ", ":-------------------------------"],
                      "state": [" State              ", ":-------------------"]}


def addTask(task):
    max_size = len(message["tasks"][1])
    for i in range(max_size - len(task) + 1):
        # Add the difference of spaces between max size and task size.
        task += " "
    # Add the task to tasks array
    message["tasks"].append(task)
    # Add the state to states array
    message["state"].append(" :white_check_mark: ")


def addError(task):
    max_size = len(message["tasks"][1])
    for i in range(max_size - len(task) + 1):
        # Add the difference of spaces between max size and task size.
        task += " "
    # Add the task to tasks array
    message["tasks"].append(task)
    # Add the state to states array
    message["state"].append(" :no_entry:         ")


def format_data():
    formatted_data = ""

    # Spaces are already accounted when tasks are added.
    for i in range(len(message["tasks"])):
        formatted_data += (
                "|"
                + message["tasks"][i]
                + "|"
                + message["state"][i]
                + "|\n"
        )
    return formatted_data


def send_mattermost_notification():

    # Format data to be prepared to be sent.
    formatted_data = format_data()

    payload = {
        "icon_url": "https://www.mattermost.org/wp-content/uploads/2016/04/icon.png",
        "text": formatted_data,
    }

    try:
        # Post request on Mattermost TSE server
        req = requests.post(hook, json=payload)
        # Raise error if request was not accepted.
        req.raise_for_status()

    except Exception as e:
        logging.error("Mattermost notification not sent")