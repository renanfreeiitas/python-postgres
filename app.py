from user import User

my_user = User('cristian@gmail.com', 'Cristian', 'Sousa', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('renato@gmail.com')

print(user_from_db)
