from src.api.data_scheme import User


class BusinessLogic:
    def __init__(self):
        self.users = [User(0, "Wojciech", "Oczkowski", 1998, "premium")]
        self.id_counter = len(self.users)

    def get_all_users(self):
        return [user.to_json() for user in self.users]

    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user.to_json()
        return None

    def create_user(self, first_name, last_name, birth_year, group):
        user_id = self.id_counter
        self.id_counter += 1
        new_user = User(user_id, first_name, last_name, birth_year, group)
        self.users.append(new_user)
        return new_user.to_json()

    def update_user(self, user_id, user_data):
        for user in self.users:
            if user.id == user_id:
                for key, value in user_data.items():
                    setattr(user, key, value)
                return user.to_json()
        return None

    def delete_user(self, user_id):
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        return False

