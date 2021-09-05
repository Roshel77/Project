
first_sec = int(input('Введите время в секундах: '))
hours = first_sec // 3600
second_sec = first_sec % 3600
minutes = second_sec // 60
last_sec = second_sec % 60

print(f'{hours:02} : {minutes:02} : {last_sec:02}')




