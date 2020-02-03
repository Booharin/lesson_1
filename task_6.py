current_distance = int(input('Ваша екущая дистанция: '))
result_distance = int(input('Ваша желаемая дистанция: '))

day_number = 1

while True:
    if current_distance >= result_distance:
        break
    current_distance = current_distance * 1.1
    day_number += 1
print(f'Необходимое число дней {day_number}')