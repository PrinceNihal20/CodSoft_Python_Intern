import json
import os
from typing import List, Dict, Any

# Define the file path for data persistence
DATA_FILE = 'todo.json'

def load_tasks() -> List[Dict[str, Any]]:
    """Loads tasks from the JSON file. If the file doesn't exist, returns an empty list."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                # Load JSON data, handling empty file case
                content = f.read()
                if content:
                    return json.loads(content)
                return []
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {DATA_FILE}. Starting with an empty list.")
        return []

def save_tasks(tasks: List[Dict[str, Any]]):
    """Saves the current list of tasks to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            # Use indent for human-readable formatting
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")

def get_next_id(tasks: List[Dict[str, Any]]) -> int:
    """Calculates the next available unique ID for a new task."""
    if not tasks:
        return 1
    # Find the maximum existing ID and add 1
    return max(task['id'] for task in tasks) + 1

def display_menu():
    """Prints the main application menu options."""
    print("\n" + "="*40)
    print("      Python CLI To-Do List Manager")
    print("="*40)
    print("1. View To-Do List")
    print("2. Add New Task")
    print("3. Mark Task Complete/Incomplete")
    print("4. Delete Task")
    print("5. Exit")
    print("="*40)

def view_tasks(tasks: List[Dict[str, Any]]):
    """Displays the current list of tasks in a formatted way."""
    if not tasks:
        print("\nYour to-do list is empty! Time to add some tasks.")
        return

    print("\n--- Current To-Do List ---")
    print(f"{'ID':<4} | {'Status':<12} | {'Task Description'}")
    print("-" * 50)

    for task in tasks:
        status_symbol = "✅ COMPLETE" if task['complete'] else "⏳ PENDING"
        print(f"{task['id']:<4} | {status_symbol:<12} | {task['description']}")
    print("-" * 50)

def add_task(tasks: List[Dict[str, Any]]):
    """Prompts the user for a task description and adds it to the list."""
    description = input("Enter the new task description: ").strip()
    if description:
        new_id = get_next_id(tasks)
        new_task = {
            'id': new_id,
            'description': description,
            'complete': False
        }
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"\nTask '{description}' added with ID {new_id}.")
    else:
        print("\nTask description cannot be empty.")

def toggle_task_status(tasks: List[Dict[str, Any]]):
    """Allows the user to change the completion status of a task by ID."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_id = int(input("Enter the ID of the task to toggle its status: "))
    except ValueError:
        print("\nInvalid input. Please enter a number for the ID.")
        return

    # Find the task by ID
    task_found = next((t for t in tasks if t['id'] == task_id), None)

    if task_found:
        task_found['complete'] = not task_found['complete']
        save_tasks(tasks)
        status = "COMPLETE" if task_found['complete'] else "INCOMPLETE"
        print(f"\nTask {task_id}: '{task_found['description']}' is now marked as {status}.")
    else:
        print(f"\nError: No task found with ID {task_id}.")

def delete_task(tasks: List[Dict[str, Any]]):
    """Allows the user to delete a task by ID."""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_id = int(input("Enter the ID of the task to DELETE: "))
    except ValueError:
        print("\nInvalid input. Please enter a number for the ID.")
        return

    # Find the task index
    try:
        index_to_delete = next(i for i, t in enumerate(tasks) if t['id'] == task_id)
        deleted_task = tasks.pop(index_to_delete)
        save_tasks(tasks)
        print(f"\nSuccessfully deleted task {task_id}: '{deleted_task['description']}'.")
    except StopIteration:
        print(f"\nError: No task found with ID {task_id}.")

def main():
    """The main function to run the To-Do List application loop."""
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            toggle_task_status(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nSaving final list and exiting. Goodbye!")
            save_tasks(tasks) # Ensure final save before exit
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

# Entry point of the script
if __name__ == "__main__":
    main()
