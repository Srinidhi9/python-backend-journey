from user import User


class AdminUser(User):
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    def get_role(self):  # method overriding
        return "Admin"

    def get_permissions(self):
        return self.permissions