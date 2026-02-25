class User:
    def __init__(self, username, email):
        self._username = username
        self._email = email

    def get_details(self):
        return f"User: {self._username}, Email: {self._email}"

    def get_role(self):
        return "User"