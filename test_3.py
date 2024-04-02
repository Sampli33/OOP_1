from solution_3 import NotSleeping

person = NotSleeping('Олег')
person.add_sheep()
person.add_sheep()
person.add_sheep()
person.add_sheep()
person.add_sheep()
print(f'{person.name}: {person.get_count_sheeps()}')
person.lost()
person.add_sheep()
person.add_sheep()
print(f'{person.name}: {person.get_count_sheeps()}')
