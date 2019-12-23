name = input('Ваше имя: ')
surname = input('Ваше Фамилия: ')
age = int(input('Ваш возраст: '))

ale = 71
alive = None

if age >= ale or age <= 0:
    alive = 0
else:
    alive = ale - age

print(f"{name} {surname}, по статистике вам осталось жить: {alive} лет")