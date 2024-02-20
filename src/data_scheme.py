class User:
    def __init__(self, user_id, first_name, last_name, birth_year, group):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.group = group

    def json(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": 2024 - self.birth_year,
            "group": self.group
        }