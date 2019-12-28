input_seconds = int(input('Введите время в секундах: '))

hours = input_seconds // 3600
minutes = (input_seconds % 3600) // 60
seconds = (input_seconds % 3600) % 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")
