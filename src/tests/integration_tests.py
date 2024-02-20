import unittest
from src.api.app import app


class TestApiIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_user_lifecycle(self):
        """
        Test user lifecycle: create, read, update, delete
        """
        new_user_data = {'first_name': 'Jakub', 'last_name': 'Teterycz', 'birth_year': 1995, 'group': 'user'}
        response = self.app.post('/users', json=new_user_data)
        self.assertEqual(response.status_code, 201)

        new_user_id = response.json['id']

        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        users_list = response.json
        self.assertTrue(any(user['id'] == new_user_id for user in users_list))

        updated_user_data = {'first_name': 'Jakub Updated', 'last_name': 'Teterycz Updated'}
        response = self.app.patch(f'/users/{new_user_id}', json=updated_user_data)
        self.assertEqual(response.status_code, 200)

        response = self.app.get(f'/users/{new_user_id}')
        self.assertEqual(response.status_code, 200)
        updated_user = response.json
        self.assertEqual(updated_user['first_name'], 'Jakub Updated')
        self.assertEqual(updated_user['last_name'], 'Teterycz Updated')

        response = self.app.delete(f'/users/{new_user_id}')
        self.assertEqual(response.status_code, 204)

        response = self.app.get(f'/users/{new_user_id}')
        self.assertEqual(response.status_code, 404)

    def test_put_route_update_or_create_user(self):
        """
        PUT /users/<int:user_id> should update user if exists or create a new one if not
        """
        existing_user_data = {'first_name': 'Existing', 'last_name': 'User', 'birth_year': 1990, 'group': 'user'}
        response = self.app.post('/users', json=existing_user_data)
        existing_user_id = response.json['id']

        updated_user_data = {'first_name': 'Updated', 'last_name': 'User'}
        response = self.app.patch(f'/users/{existing_user_id}', json=updated_user_data)
        self.assertEqual(response.status_code, 200)

        response = self.app.get(f'/users/{existing_user_id}')
        self.assertEqual(response.status_code, 200)
        updated_user = response.json
        self.assertEqual(updated_user['first_name'], 'Updated')

        new_user_data = {'first_name': 'New', 'last_name': 'User'}
        response = self.app.patch(f'/users/{existing_user_id}', json=new_user_data)
        self.assertEqual(response.status_code, 200)

        response = self.app.get(f'/users/{existing_user_id}')
        self.assertEqual(response.status_code, 200)
        updated_user = response.json
        self.assertEqual(updated_user['first_name'], 'New')


if __name__ == '__main__':
    unittest.main()
