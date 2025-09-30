📞 Simple Contact Book Application
This is a full-stack web application designed to manage personal and professional contacts. It is built using Python (Flask) for the backend API and HTML, CSS, and vanilla JavaScript for a dynamic, user-friendly frontend.

This project was developed to meet the requirements of TASK 5 for a contact management system.

✨ Features
The application implements the following core functionalities:

Feature

Description

Implementation

Contact Information

Stores Name, Phone Number (required), Email, and Address (optional) for each entry.

Managed via JSON objects in the Flask server's memory.

Add Contact

Users can input new details via the form and submit them to the server.

POST request to /api/contacts.

View Contact List

Displays all saved contacts with primary details (Name and Phone).

GET request to /api/contacts.

Search Contact

Allows real-time filtering of the list by searching against Name or Phone Number.

Handled client-side using JavaScript for instant results.

Update Contact

The "Edit" button populates the form, enabling users to modify and save existing details.

PUT request to /api/contacts/<id>.

Delete Contact

The "Delete" button removes a contact entry from the list after confirmation.

DELETE request to /api/contacts/<id>.

⚙️ Setup and Installation
Prerequisites
You need to have Python installed on your system.

1. File Structure
Ensure your project files are organized in the following structure for Flask to correctly find the templates and static assets:

contact_book_app/
├── app.py
├── static/
│   └── style.css
└── templates/
    └── index.html

2. Install Dependencies
Open your terminal or command prompt and install the necessary Python package (Flask):

pip install Flask

3. Run the Application
Navigate into the root directory of your project (contact_book_app) and execute the Python file:

python app.py

4. Access the App
Once the server is running, open your web browser and navigate to the local host address displayed in the terminal:

👉 http://127.0.0.1:5000/

💡 Important Note on Persistence
This is a demonstration application using a simple Python list (contacts) for data storage.

Data is stored only in the server's memory. If you stop the server and restart it, all contacts added during the session will be lost, and the application will revert to the two initial default contacts (Alice Smith and Bob Johnson).

For a production environment, this application would require integration with a database (e.g., SQLite, PostgreSQL, or Firestore).