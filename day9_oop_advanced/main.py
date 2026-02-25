from admin_user import AdminUser
from savings_account import SavingsAccount

admin = AdminUser("Srinidhi", "sri@email.com", ["add_user", "delete_user"])
print(admin.get_details())
print("Role:", admin.get_role())
print("Permissions:", admin.get_permissions())

account = SavingsAccount("Srinidhi", 1000, 5)
account.deposit(500)
account.add_interest()
print("Balance:", account.get_balance())