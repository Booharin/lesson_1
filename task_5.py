revenue = int(input('Ваша выручка: '))
costs = int(input('Вашы расходы: '))

profit = revenue - costs

if profit > 0:
    print(f"Ваша прибыль составила: {profit}")
    print(f"Рентабельность: {(profit / revenue) * 100:.3f}%")

    staff_number = int(input('Количество сотрудников: '))
    print(f"Прибыль на одного сотрудника: {(profit / staff_number):.3f}")
else:
    print(f"Нихрена вы не заработали")
