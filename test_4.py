from solution_4 import User

user_1 = User(12, 'alex', 'Алексей')
print(user_1)
user_2 = User(44, 'andru', 'Андрей', 'Петров')
print(user_2)
user_3 = User(25, 'nik', 'Николай', 'Иванов', 'Федорович')
print(user_3)
user_4 = User(61, 'ivan', 'Денис', 'Сидоров', 'Алексеевич', 'M')
print(user_4)
user_5 = User(47, 'ann', 'Анна', gender='F')
print(user_5)
user_4.update(id='55', gender='F')
print(user_4)
user_1.update(last_name='Петров', gender='M')
print(user_1)
user_2.update()
print(user_2)
