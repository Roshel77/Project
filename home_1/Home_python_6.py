
first_res = int(input('Ваш результат в первый день пробежки: '))
last_res = int(input('Результат, к которому вы стремитесь: '))
n = 1
day = 1
first_res1 = first_res
while first_res < last_res:
    day = day + 1
    first_res = first_res1 * (1.1 ** n)
    n = n + 1
print(f'Поставленной цели вы достигните на {day} день')


