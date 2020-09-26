time = int(input('Введите время в секундах: '))
seconds = time % 60
minutes = time // 60
hours = minutes // 60
print(f'{hours}:{minutes}:{seconds}')