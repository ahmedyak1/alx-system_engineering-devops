#!/usr/bin/python3
"""program that uses an API to get details about a certain employee's ID
"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    user_url = '{}/users?id={}'.format(base_url, user_id)

    response = requests.get(user_url)
    # pull data from API
    data = response.text
    # convert the data into JSON format
    data = json.loads(data)
    # get the user data, in this case, username of employeee
    user_name = data[0].get('username')

    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    response = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)

    # create the csv
    builder = ""
    for task in tasks:
        builder += '"{}","{}","{}","{}"\n'.format(
            user_id,
            user_name,
            task['completed'],  # or use get method
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(builder)

