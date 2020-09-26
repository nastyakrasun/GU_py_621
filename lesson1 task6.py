result = int(input('Расстояние, которое пробежали сегдня, км: '))
day_number = 1
max = int(input('Максимальное расстояние, км: '))
while result < max:
    day_number += 1
    result = 1.1 * result
print(f'На {day_number} день общий результат спортсмена составит не менее {max} километров ({round(result, 2)} км)')
