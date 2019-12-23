number = int(input("Введите число n: "))

item_2 = f"{number}{number}"
item_3 = f"{number}{number}{number}"

total_sum = number + int(item_2) + int(item_3)

print(f"Sum: {total_sum}")
