from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simple in-memory storage for contacts
# In a real application, you would use a database (e.g., SQLite, PostgreSQL)
contacts = [
    {"id": 1, "name": "Alice Smith", "phone": "123-456-7890", "email": "alice@example.com", "address": "123 Main St"},
    {"id": 2, "name": "Bob Johnson", "phone": "987-654-3210", "email": "bob@example.com", "address": "456 Oak Ave"},
]
current_id = 3

@app.route('/')
def index():
    """Renders the main contact book HTML page."""
    return render_template('index.html')

# --- API Endpoints ---

@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    """API to get all contacts (View Contact List)."""
    # Note: Search is handled on the client-side (JavaScript) for this simple app
    return jsonify(contacts)

@app.route('/api/contacts', methods=['POST'])
def add_contact():
    """API to add a new contact."""
    global current_id
    new_contact = request.get_json()
    
    # Validation (minimal)
    if not all(k in new_contact for k in ('name', 'phone')):
        return jsonify({"error": "Missing required fields (name, phone)"}), 400
        
    new_contact['id'] = current_id
    # Ensure optional fields exist, even if empty
    new_contact['email'] = new_contact.get('email', '')
    new_contact['address'] = new_contact.get('address', '')
    
    contacts.append(new_contact)
    current_id += 1
    return jsonify({"message": "Contact added successfully", "contact": new_contact}), 201

@app.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    """API to update an existing contact."""
    update_data = request.get_json()
    for contact in contacts:
        if contact['id'] == contact_id:
            # Update the existing contact's dictionary with the received data
            contact.update(update_data) 
            return jsonify({"message": "Contact updated successfully", "contact": contact})
    return jsonify({"error": "Contact not found"}), 404

@app.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    """API to delete a contact."""
    global contacts
    initial_length = len(contacts)
    # Filter out the contact with the matching ID
    contacts = [contact for contact in contacts if contact['id'] != contact_id]
    
    if len(contacts) < initial_length:
        return jsonify({"message": "Contact deleted successfully"})
    return jsonify({"error": "Contact not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)