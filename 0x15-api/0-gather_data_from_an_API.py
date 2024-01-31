#!/usr/bin/python3
"""program that uses an API to get details about a certain employee's ID"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get info user from https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)

    # get it from API

    response = requests.get(user_url)

    data = response.text
    # convert the information to JSON format.
    data = json.loads(data)
 
    name = data[0].get('name')

    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    response = requests.get(tasks_url)

    tasks = response.text
    # parse the data into JSON format
    tasks = json.loads(tasks)

    completed = 0
    total_tasks = len(tasks)

    completed_tasks = []
    # loop through tasks counting number of completed tasks
    for task in tasks:

        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))




