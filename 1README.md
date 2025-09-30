📝 Python CLI To-Do List Manager
A simple yet effective command-line application for managing your daily tasks. This project demonstrates fundamental Python programming concepts, including list manipulation, file I/O (using JSON for persistence), and building a basic command-line interface (CLI).

✨ Features
The application provides a straightforward interface to perform the following actions on your task list:

View Tasks: Display all tasks with their unique IDs and completion status.

Add Tasks: Easily add new tasks to your list.

Toggle Status: Mark tasks as COMPLETE or PENDING.

Delete Tasks: Permanently remove tasks from the list using their ID.

Data Persistence: All tasks are automatically saved to a local file (todo.json) and reloaded the next time you run the app.

🚀 How to Run
Requirements
You only need Python 3.x installed on your system.

Steps
Save the file: Ensure the Python code (todo_cli_app.py) is saved in a local folder.

Open Terminal: Navigate to that folder using your terminal or command prompt (or use the integrated terminal in VS Code).

Execute the script: Run the application using the following command:

python todo_cli_app.py

📋 Usage Guide
Once the application starts, you will be presented with the main menu. Simply enter the number corresponding to the action you wish to perform and press Enter.

Main Menu
========================================
      Python CLI To-Do List Manager
========================================
1. View To-Do List
2. Add New Task
3. Mark Task Complete/Incomplete
4. Delete Task
5. Exit
========================================
Enter your choice (1-5):