data = []
fields = ('название', 'цена', 'количество', 'ед.')
# i = 1
while True:
    prod_num = int(input('Введите номер товара: '))
    products = {}
    for i in fields:
        products[i] = input(f'Введите {i}: ')
    data.append(products)
    if input('Добавить еще один товар? (да/нет): ') == 'нет':
        break
print(f'Список товаров:{data}')



#     products.append(
#         (input('Введите номер товара: '), dict({
#             'название': str(input('Введите название: ')),
#             'цена': float(input('Введите цену: ')),
#             'количество': int(input('Введите количество: ')),
#             'eд': str(input('Введите единцы измерения: ')),
#         }))
#     )
#
#     if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
#         break
#
#     i += 1
#
# print(f'список товаров:{inventory_tuple_list}')
#
# output_dict = dict({})
# for product in inventory_tuple_list:
#     for key, value in product[-1].items():
#         if key in output_dict:
#             if value not in output_dict.get(key):
#                 output_dict.get(key).append(value)
#         else:
#             output_dict.update({key: [value]})
#
#
# print(f'собрана аналитика: {output_dict}')