from database import Database
from user import User

Database.initialise(database="exercises", host="localhost", user="postgres", password="password")

user = User('pedro@gmail.com', 'Pedro', 'Guerra', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('renanfreitas@gmail.com')

print(user_from_db)
