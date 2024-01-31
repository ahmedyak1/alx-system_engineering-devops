#!/usr/bin/python3
"""program which employs an API to get information on a specific employee's ID"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    user_url = '{}/users?id={}'.format(base_url, user_id)

    # get inf  from api
    response = requests.get(user_url)
    # pull data 
    data = response.text
    # Convert  the data into JSON forma
    data = json.loads(data)
    # extract user data, in this case, name of employee
    name = data[0].get('name')
    # print("name is: {}".format(name))

    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)
    # print("tasks url is: {}".format(tasks_url))

    # get data  from api
    response = requests.get(tasks_url)
    # pull data from api
    tasks = response.text
    tasks = json.loads(tasks)

    completed = 0
    total_tasks = len(tasks)

    completed_tasks = []
    # loop through tasks counting number of completed tasks
    for task in tasks:

        if task.get('completed'):
            # print("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # print the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
