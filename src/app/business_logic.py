from src.app.data_scheme import User


class BusinessLogic:
    def __init__(self):
        self.users = []
        self.id_counter = 1

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

    def is_valid_user_data(self, user_data):
        valid_groups = ["user", "premium", "admin"]
        if all(key in user_data for key in ["firstName", "lastName", "birthYear", "group"]):
            if isinstance(user_data["birthYear"], int) and user_data["birthYear"] > 0:
                if user_data["group"] in valid_groups:
                    return True
        return False

