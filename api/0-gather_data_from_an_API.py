#!/usr/bin/python3
"""Fetch and display employee TODO list progress from a REST API."""

import requests
import sys


if __name__ == "__main__":
    # Ensure exactly one argument (employee ID)
    if len(sys.argv) != 2:
        sys.exit()

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit()

    # API URLs
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # API requests
    user_res = requests.get(user_url)
    todos_res = requests.get(todos_url)

    if user_res.status_code != 200 or todos_res.status_code != 200:
        sys.exit()

    # Process data
    employee_name = user_res.json().get("name")
    todos = todos_res.json()

    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    # Display output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
