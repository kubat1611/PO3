class BusinessLogic:
    def __init__(self):
        self.users = []
        self.id_counter = 1

    def get_all_users(self):
        return [user.json() for user in self.users]