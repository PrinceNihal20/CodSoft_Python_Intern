Secure Password Generator
This is a full-stack web application designed to generate strong, customizable, and random passwords. The core generation logic is handled by a Python Flask backend, while the user interface and interaction are managed by a modern HTML/Tailwind CSS frontend.

✨ Features
Customizable Length: Users can select a password length between 6 and 64 characters using a range slider.

Complexity Options: Allows users to include/exclude:

Uppercase letters (A-Z)

Numbers (0-9)

Symbols (!@#$%^&*, etc.)

Real-time Generation: Generates a new password upon request via an API call to the Flask server.

Copy Functionality: Easily copy the generated password to the clipboard with a single click.

Responsive Design: Optimized for display on both desktop and mobile devices.

💻 Technologies Used
Backend
Python 3: Core programming language.

Flask: Lightweight web framework for handling the API endpoint.

Flask-CORS: Used to enable Cross-Origin Resource Sharing, allowing the frontend (on a different port) to access the backend API.

Frontend
HTML5: Structure of the web application.

Tailwind CSS: Utility-first CSS framework for styling and responsive design.

JavaScript (ES6+): Handles user interactions, API calls, and displaying the generated password.

🚀 Setup and Running Instructions
To run this project, you need to start the Python backend server first, and then open the HTML frontend in your browser.

1. Backend Setup (password_generator_server.py)
Install Python: Ensure you have Python 3.x installed on your system.

Install Dependencies: Open your terminal and install the required packages:

pip install flask flask-cors

Run the Server: Navigate to the directory containing password_generator_server.py and execute the script:

python password_generator_server.py

The server will start and run on http://localhost:5000. Keep this terminal window open.

2. Frontend Access (index.html)
The frontend must be accessed via a local web server (like VS Code's Live Server extension) so it can successfully communicate with the Flask API.

Install VS Code Extension: If you are using VS Code, install the Live Server extension (by Ritwick Dey).

Open the HTML File: Right-click on the index.html file in your editor or file explorer.

Launch: Select Open with Live Server.

The web application will open in your browser, and the "Generate Password" button will now successfully communicate with the Python backend running on port 5000.

🛠️ Usage
Set Length: Move the Password Length slider to the desired value (e.g., 20).

Select Complexity: Check the boxes for Uppercase Letters, Numbers, and Symbols to include them in the generated password.

Generate: Click the Generate Password button.

Copy: Click the copy icon next to the generated password to quickly save it to your clipboard.