from db.repo import UserService


users = [user.get('id') for user in UserService.get_all_users()]

print(users)
