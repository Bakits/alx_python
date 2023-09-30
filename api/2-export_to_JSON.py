"""
2-export_to_JSON.py - Export Employee's TODO List Data to JSON

This script fetches information about an employee's TODO list from a REST API and exports it to a JSON file.

Requirements:
- You must use the requests and json modules.
- The script must accept an integer as a parameter, which is the employee ID.
- The script displays the employee's TODO list progress in the console and exports it to a JSON file.

Example:
    To export the TODO list for an employee with ID 2:
    $ python3 2-export_to_JSON.py 2

JSON File Format:
    {
        "USER_ID": [
            {
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS,
                "username": "USERNAME"
            },
            ...
        ]
    }

Module Dependencies:
    - requests: Used for making HTTP requests to the API.
    - json: Used for working with JSON data.

Functions:
    - get_employee_todo_progress(employee_id): Fetches and exports employee TODO list data in JSON format.
        - Parameters:
            - employee_id (int): The ID of the employee to fetch data for.

Usage:
    Run this script with an employee ID as a command-line argument to fetch and export the data.

"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches employee's TODO list and exports it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch user information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        user_id = user_data.get("id", "Unknown")
        user_name = user_data.get("name", "Unknown")

        # Fetch TODO list for the user
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Create JSON data
        json_data = {str(user_id): []}
        for task in todos_data:
            json_data[str(user_id)].append(
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_name,
                }
            )

        # Export data to JSON file
        json_filename = f"{user_id}.json"
        with open(json_filename, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
