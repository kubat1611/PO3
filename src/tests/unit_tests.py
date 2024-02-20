import unittest
from src.api.business_logic import BusinessLogic


class TestBusinessLogicUnit(unittest.TestCase):

    def setUp(self):
        self.business_logic = BusinessLogic()

    def test_get_all_users(self):
        users = self.business_logic.get_all_users()
        self.assertIsInstance(users, list)
        self.assertTrue(all(isinstance(user, dict) for user in users))

    def test_get_user(self):
        existing_user_id = 0
        non_existing_user_id = 999

        existing_user = self.business_logic.get_user(existing_user_id)
        non_existing_user = self.business_logic.get_user(non_existing_user_id)

        self.assertIsInstance(existing_user, dict)
        self.assertEqual(existing_user['id'], existing_user_id)

        self.assertIsNone(non_existing_user)

    def test_update_user(self):
        user_id = 0
        initial_user = self.business_logic.get_user(user_id)

        update_data = {'first_name': 'UpdatedFirst_Name', 'last_name': 'UpdatedLast_Name'}
        updated_user = self.business_logic.update_user(user_id, update_data)

        self.assertIsInstance(updated_user, dict)
        self.assertEqual(updated_user['id'], user_id)
        self.assertEqual(updated_user['first_name'], update_data['first_name'])
        self.assertEqual(updated_user['last_name'], update_data['last_name'])

        self.assertEqual(updated_user['age'], initial_user['age'])
        self.assertEqual(updated_user['group'], initial_user['group'])

    def test_create_user(self):
        initial_user_count = len(self.business_logic.users)

        new_user_data = {'first_name': 'John', 'last_name': 'Doe', 'birth_year': 1990, 'group': 'user'}
        new_user = self.business_logic.create_user(**new_user_data)

        self.assertIsInstance(new_user, dict)
        self.assertIn('id', new_user)

        updated_user_count = len(self.business_logic.users)
        self.assertEqual(updated_user_count, initial_user_count + 1)

    def test_delete_user(self):
        user_id = 0
        initial_user_count = len(self.business_logic.users)

        deleted = self.business_logic.delete_user(user_id)

        self.assertTrue(deleted)

        updated_user_count = len(self.business_logic.users)
        self.assertEqual(updated_user_count, initial_user_count - 1)

    def test_is_valid_user_data(self):
        valid_user_data = {'first_name': 'John', 'last_name': 'Doe', 'birth_year': 1990, 'group': 'user'}
        invalid_user_data = {'first_name': 'John', 'birth_year': 1990, 'group': 'invalid_group'}

        valid_result = self.business_logic.is_valid_user_data(valid_user_data)
        invalid_result = self.business_logic.is_valid_user_data(invalid_user_data)

        self.assertTrue(valid_result)
        self.assertFalse(invalid_result)


if __name__ == '__main__':
    unittest.main()
