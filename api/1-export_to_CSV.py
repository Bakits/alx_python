"""
1-export_to_CSV.py - Export Employee's TODO List Data to CSV

This script fetches information about an employee's TODO list from a REST API and exports it to a CSV file.

Requirements:
- You must use the requests and csv modules.
- The script must accept an integer as a parameter, which is the employee ID.
- The script displays the employee's TODO list progress in the console and exports it to a CSV file.

Example:
    To export the TODO list for an employee with ID 2:
    $ python3 1-export_to_CSV.py 2

CSV File Format:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

Module Dependencies:
    - requests: Used for making HTTP requests to the API.
    - csv: Used for working with CSV files.

Functions:
    - get_employee_todo_progress(employee_id): Fetches and displays employee TODO list progress.
        - Parameters:
            - employee_id (int): The ID of the employee to fetch data for.

Usage:
    Run this script with an employee ID as a command-line argument to fetch and export the data.

"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches employee's TODO list and exports it to a CSV file.

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

        # Calculate the number of completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for task in todos_data if task["completed"])

        # Display employee TODO list progress
        print(
            f"Employee {user_name} is done with tasks({completed_tasks}/{total_tasks}):"
        )
        for task in todos_data:
            if task["completed"]:
                print(f"    {task['title']}")

        # Export data to CSV file
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            )
            for task in todos_data:
                csv_writer.writerow(
                    [user_id, user_name, str(task["completed"]), task["title"]]
                )

        print(f"Data exported to {csv_filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
