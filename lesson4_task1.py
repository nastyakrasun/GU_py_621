# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.

import sys

def salary(time, pay, extra):
    result = (time * pay) + extra  # В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    print(result)
    return result

command = sys.argv[1]  # Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
if command == 'salary':
    time = float(sys.argv[2])
    pay = float(sys.argv[3])
    extra = float(sys.argv[4])
    salary(time, pay, extra)