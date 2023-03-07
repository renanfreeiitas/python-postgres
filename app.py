from user import User

my_user = User('joao@gmail.com', 'Joao', 'Hernandez', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('renato@gmail.com')

print(user_from_db)



'''
apenas testando funcionalidade do codigo junto ao repositorio do github
'''


'''
novo teste de nuva branch
'''