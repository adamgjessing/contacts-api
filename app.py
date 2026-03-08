from flask import Flask, jsonify, request
from database import get_db, create_table

app = Flask(__name__)

@app.route('/contacts', methods=['GET'])
def get_contacts():
    conn = get_db()
    contacts = conn.execute('SELECT * FROM contacts').fetchall()
    conn.close()
    return jsonify([dict(contact) for contact in contacts])

@app.route('/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    conn = get_db()
    contact = conn.execute(
        'SELECT * FROM contacts WHERE id = ?', (id,)
    ).fetchone()
    conn.close()
    if contact is None:
        return jsonify({"error": "Contact not found"}), 404
    return jsonify(dict(contact))

@app.route('/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400
    conn = get_db()
    conn.execute(
        'INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)',
        (data['name'], data['email'], data.get('phone'))
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Contact created successfully!"}), 201

@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    data = request.get_json()
    conn = get_db()
    contact = conn.execute(
        'SELECT * FROM contacts WHERE id = ?', (id,)
    ).fetchone()
    if contact is None:
        return jsonify({"error": "Contact not found"}), 404
    conn.execute('''
        UPDATE contacts 
        SET name = ?, email = ?, phone = ?
        WHERE id = ?
    ''', (
        data.get('name', contact['name']),
        data.get('email', contact['email']),
        data.get('phone', contact['phone']),
        id
    ))
    conn.commit()
    conn.close()
    return jsonify({"message": "Contact updated successfully!"})

@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    conn = get_db()
    conn.execute('DELETE FROM contacts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Contact deleted successfully!"})

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
