import json
import requests


def fetch_employee_todo_progress(employee_id):
    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return []

    return todos_response.json()


def export_todo_all_employees_to_json():
    all_employee_data = {}

    # Fetch TODO progress for all employees (assuming employee IDs are consecutive integers)
    for employee_id in range(1, 11):  # Assuming 10 employees with IDs from 1 to 10
        todos_data = fetch_employee_todo_progress(employee_id)

        # Fetch employee details
        employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        employee_response = requests.get(employee_url)

        if employee_response.status_code == 200:
            employee_data = employee_response.json()
            employee_username = employee_data['username']

            # Create a list to store tasks for the employee
            employee_tasks = []

            # Iterate through the tasks and transform them
            for task in todos_data:
                task_data = {
                    "username": employee_username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
                employee_tasks.append(task_data)

            # Store the employee's tasks in the dictionary under their ID
            all_employee_data[str(employee_id)] = employee_tasks

    # Create JSON file and write data for all employees
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employee_data, json_file, indent=4)


if __name__ == "__main__":
    export_todo_all_employees_to_json()
