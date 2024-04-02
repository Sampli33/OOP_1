from solution_2 import NotSleeping

person = NotSleeping('Олег')
person.add_sheep()
person.add_sheep()
person.add_sheep()
person.add_sheep()
print(f'{person.name}: {person.get_value}')
person.__value = 0
print(f'{person.name}: {person.get_value}')
