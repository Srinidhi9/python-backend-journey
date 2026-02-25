class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in.")

    def logout(self):
        print(f"{self.username} logged out.")