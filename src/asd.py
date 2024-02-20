import requests

# Set the base URL for your API
base_url = "http://127.0.0.1:5000/"


def _user_lifecycle():
    # Create a new user
    new_user_data = {'first_name': 'sdsdds', 'last_name': 'sddsdsz', 'birth_year': 1995, 'group': 'admin'}
    response = requests.post(f'{base_url}/users', json=new_user_data)
    assert response.status_code == 201

    new_user_id = response.json()['id']
    print(new_user_id)

    # Read the list of users
    response = requests.get(f'{base_url}/users')
    assert response.status_code == 200
    users_list = response.json()
    print(users_list)
    assert any(user['id'] == new_user_id for user in users_list)


    # Update the user
    updated_user_data = {'first_name': 'Jakub Updated', 'last_name': 'Teterycz Updated'}
    response = requests.patch(f'{base_url}/users/{new_user_id}', json=updated_user_data)
    print(response.status_code)
    assert response.status_code == 200

    # Read the updated user
    response = requests.get(f'{base_url}/users/{new_user_id}')
    assert response.status_code == 200
    updated_user = response.json()
    print(updated_user)
    assert updated_user['first_name'] == 'Jakub Updated'
    assert updated_user['last_name'] == 'Teterycz Updated'

    # Delete the user
    response = requests.delete(f'{base_url}/users/{new_user_id}')
    assert response.status_code == 204

    # Verify that the user is deleted
    response = requests.get(f'{base_url}/users/{new_user_id}')
    assert response.status_code == 404


if __name__ == "__main__":
    _user_lifecycle()
