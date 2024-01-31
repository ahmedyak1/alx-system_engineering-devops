#!/usr/bin/python3
"""Code info about all employees using an API and exports it in json format
"""
import json
import requests


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    # get users info e.g https://jsonplaceholder.typicode.com/users
    users_url = '{}/users'.format(base_url)

    # get it  from api
    response = requests.get(users_url)
    # pull data from api
    data = response.text
    # convert  data into JSON format
    data = json.loads(data)

    # get users data
    builder = {}
    for user in data:
        user_id = user.get('id')

        user_name = user.get('username')

        dict_key = str(user_id)

        builder[dict_key] = []
        tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
        # print("tasks url is: {}".format(tasks_url))

        # get information from API
        response = requests.get(tasks_url)
        # pull data from api
        tasks = response.text
        # Convert the data into JSON format
        tasks = json.loads(tasks)

        for task in tasks:
            json_data = {
                "task": task['title'],  # or use get method
                "completed": task['completed'],
                "username": user_name
            }
            builder[dict_key].append(json_data)
    # write the data the file
    json_encoded_data = json.dumps(builder)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
