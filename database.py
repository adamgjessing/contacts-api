import sqlite3

def get_db():
	conn = sqlite3.connect('contacts.db')
	conn.row_factory = sqlite3.Row
	return conn

def create_table():
	conn = get_db()
	conn.execute('''
		CREATE TABLE IF NOT EXISTS contacts (
			id INTEGER PRIMARY KEY AUTOINCREMENT, 
			name TEXT NOT NULL, 
			email TEXT NOT NULL, 
			phone TEXT
		)
	''')
	conn.commit()
	conn.close()

def create_contact(name, email, phone=None):
	conn = get_db()
	conn.execute(
		'INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)',
		(name, email, phone)
	)
	conn.commit()
	conn.close()
	print(f"Contact {name} created successfully!")

def get_all_contacts():
	conn = get_db()
	contacts = conn.execute('SELECT * FROM contacts').fetchall()
	conn.close()
	return [dict(contact) for contact in contacts]

def get_contact(id):
	conn = get_db()
	contacts = conn.execute(
		'SELECT * FROM contacts WHERE id = ?', (id,)
	).fetchone()
	conn.close()
	return dict(contacts) if contact else None

def update_contact(id, name=None, email=None, phone=None):
	conn = get_db()
	contact = get_contact(id)
	if contact:
		conn.execute('''
			UPDATE contacts
			SET name = ?, email = ?, phone = ?
			WHERE id = ?
		''', (
			name or contact['name'],
			email or contact['email'],
			phone or contact['phone'], 
			id
		))
		conn.commit()
		print(f"Contact {id} updated successfully!")
	conn.close()

def delete_contact(id):
	conn = get_db()
	conn.execute('DELETE FROM contacts WHERE id = ?', (id,))
	conn.commit()
	conn.close()
	print(f"Contact {id} deleted successfully!")

			
if __name__ == '__main__':
	create_table()
	print("Database ready!")

	create_contact("Adam", "adam@email.com", "555-1234")
	create_contact("Sarah", "Sarah@email.com", "555-5678")

	print("\nAll contact:")
	for contact in get_all_contacts():
		print(contact)
	
	print("\nUpdating Adam's phone...")
	update_contact(1, phone ="555-9999")


	print("\nDeleting Sarah...")
	delete_contact(2)

	print("\nfinal contacts:")
	for contact in get_all_contacts():
		print(contact)

