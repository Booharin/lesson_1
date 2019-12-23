number = int(input("Введите число n: "))

max_number = -1

while number > 0:
    digit = number % 10
    number = number // 10
    if max_number < digit:
        max_number = digit

print(max_number)
