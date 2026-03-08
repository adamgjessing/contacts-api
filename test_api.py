import requests

BASE_URL = 'http://127.0.0.1:8080'

def test_get_empty_contacts():
    response = requests.get(f'{BASE_URL}/contacts')
    assert response.status_code == 200
    assert type(response.json()) == list
    print("✓ Get all contacts works")

def test_create_contact():
    response = requests.post(f'{BASE_URL}/contacts',
        json={
            "name": "Test User",
            "email": "test@email.com",
            "phone": "555-1234"
        })
    assert response.status_code == 201
    assert response.json()['message'] == "Contact created successfully!"
    print("✓ Create contact works")

def get_last_contact_id():
    response = requests.get(f'{BASE_URL}/contacts')
    contacts = response.json()
    return contacts[-1]['id']

def test_get_contact(id):
    response = requests.get(f'{BASE_URL}/contacts/{id}')
    assert response.status_code == 200
    assert response.json()['name'] == "Test User"
    print("✓ Get single contact works")

def test_update_contact(id):
    response = requests.put(f'{BASE_URL}/contacts/{id}',
        json={"phone": "555-9999"})
    assert response.status_code == 200
    assert response.json()['message'] == "Contact updated successfully!"
    print("✓ Update contact works")

def test_delete_contact(id):
    response = requests.delete(f'{BASE_URL}/contacts/{id}')
    assert response.status_code == 200
    assert response.json()['message'] == "Contact deleted successfully!"
    print("✓ Delete contact works")

def test_missing_contact():
    response = requests.get(f'{BASE_URL}/contacts/999')
    assert response.status_code == 404
    print("✓ 404 for missing contact works")

def test_create_without_name():
    response = requests.post(f'{BASE_URL}/contacts',
        json={"email": "test@email.com"})
    assert response.status_code == 400
    print("✓ Rejects contact without name")

if __name__ == '__main__':
    print("\nRunning API tests...\n")
    test_get_empty_contacts()
    test_create_contact()
    id = get_last_contact_id()
    test_get_contact(id)
    test_update_contact(id)
    test_delete_contact(id)
    test_missing_contact()
    test_create_without_name()
    print("\nAll tests passed!")
