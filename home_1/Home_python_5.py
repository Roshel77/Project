
revenue = float(input('Введите сумму выручки: '))
cost = float(input('Введите сумму издержек: '))

profit = revenue - cost
if revenue > cost:
    print(f'Прибыль составляет: {profit:.2f}')
    margin = profit / revenue * 100
    print(f'Рентабельность составляет: {margin:.2f}%')
    staff = int(input('Численность сотрудников: '))
    profit_per_1 = profit / staff
    print(f'Прибыль в рассчете на одного сотрудника равна: {profit_per_1:.2f}')
elif revenue == cost:
    print('Прибыль равна 0')
else:
    print('Убыток составил: ', profit)


