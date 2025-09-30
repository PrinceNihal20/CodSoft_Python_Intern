# Import necessary modules
import random
import string
from flask import Flask, request, jsonify
from flask_cors import CORS # Used to allow the frontend (running on a different port) to access the backend

# Initialize the Flask application
app = Flask(__name__)
# Enable CORS for all routes, allowing the frontend to communicate with this API
CORS(app)

# --- Core Password Generation Function ---
def generate_password(length: int, include_uppercase: bool, include_numbers: bool, include_symbols: bool) -> str:
    """
    Generates a strong, random password based on specified criteria.
    
    Args:
        length: The desired length of the password.
        include_uppercase: Whether to include uppercase letters.
        include_numbers: Whether to include digits.
        include_symbols: Whether to include punctuation symbols.
        
    Returns:
        The generated password string.
    """
    # Start with mandatory lowercase letters
    characters = string.ascii_lowercase
    
    # Initialize the password to ensure at least one character from each selected category
    password = []
    
    # Check and include optional character sets
    if include_uppercase:
        characters += string.ascii_uppercase
        # Ensure at least one uppercase letter is in the final password
        password.append(random.choice(string.ascii_uppercase))

    if include_numbers:
        characters += string.digits
        # Ensure at least one number is in the final password
        password.append(random.choice(string.digits))
        
    if include_symbols:
        # Use common, easy-to-type symbols
        symbols = '!@#$%^&*()_+-=[]{};:,.<>/?'
        characters += symbols
        # Ensure at least one symbol is in the final password
        password.append(random.choice(symbols))

    # Add lowercase letters regardless of options (as a base)
    if not include_uppercase and not include_numbers and not include_symbols:
         # If no options are selected, at least include lowercase for simplicity
         characters = string.ascii_lowercase
    else:
        # Ensure at least one lowercase letter is included if other options are present
        password.append(random.choice(string.ascii_lowercase))


    # Fill the remaining length of the password from the combined character set
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choices(characters, k=remaining_length))

    # Shuffle the resulting list of characters to ensure randomness
    random.shuffle(password)
    
    # Convert the list back into a single string
    return "".join(password)

# --- API Endpoint ---
@app.route('/generate-password', methods=['POST'])
def handle_password_generation():
    """
    Handles POST requests to generate a password.
    Expects a JSON body with 'length', 'uppercase', 'numbers', 'symbols' keys.
    """
    try:
        # Get JSON data from the request body
        data = request.get_json()
        
        # Validate and extract required parameters
        length = int(data.get('length', 12)) # Default length to 12
        
        # Length constraints for security and usability
        if not 6 <= length <= 64:
            return jsonify({'error': 'Password length must be between 6 and 64.'}), 400

        # Extract boolean complexity flags, defaulting to False if not provided
        include_uppercase = bool(data.get('uppercase', False))
        include_numbers = bool(data.get('numbers', False))
        include_symbols = bool(data.get('symbols', False))

        # Generate the password
        password = generate_password(
            length, 
            include_uppercase, 
            include_numbers, 
            include_symbols
        )

        # Return the generated password as a JSON response
        return jsonify({'password': password}), 200

    except Exception as e:
        # Log the error and return a generic server error message
        print(f"An error occurred: {e}")
        return jsonify({'error': 'An internal server error occurred during password generation.'}), 500

# --- Server Start ---
if __name__ == '__main__':
    # Run the application on http://localhost:5000
    print("Starting Flask server on http://localhost:5000/...")
    app.run(debug=True, port=5000)
