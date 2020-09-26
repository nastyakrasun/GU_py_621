profit = int(input('Введите значение выручки: '))
loss = int(input('Введите значение издержек: '))
gross_profit = profit - loss
if gross_profit > 0:
    print('Фирма отработала с прибылью')
    efficiency = (gross_profit / profit) * 100
    print('Рентабольность выручки равна:', efficiency)
    staff = int(input('Введите число сотрудников: '))
    staff_earning = gross_profit / staff
    print('Прибыль фирмы в расчёте на одного сотрудника равна:', staff_earning)
else:
    print('Фирма отработала с убытком')