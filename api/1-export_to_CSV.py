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

# Function to fetch tasks for a specific user
def fetch_tasks(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()
    return tasks

# Function to export tasks to a CSV file
def export_to_csv(user_id, tasks):
    filename = f"{USER_ID}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": "Antonette",  # You can replace this with any username of your choice
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_id = int(user_id)
    except ValueError:
        print("USER_ID must be an integer.")
        sys.exit(1)

    tasks = fetch_tasks(user_id)
    export_to_csv(USER_ID, tasks)
    print(f"Data exported to {USER_ID}.csv")
