#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
table_code = goods['Стол']

table1_quantity = store[table_code][0]['quantity']
table1_price = store[table_code][0]['price']
table1_cost = table1_quantity * table1_price

table2_quantity = store[table_code][1]['quantity']
table2_price = store[table_code][1]['price']
table2_cost = table2_quantity * table2_price

table_total_quantity = table1_quantity + table2_quantity
table_total_cost = table1_cost + table2_cost
print(f'Стол - {table_total_quantity} шт, стоимость {table_total_cost} руб')

divan_code = goods['Диван']

divan1_quantity = store[divan_code][0]['quantity']
divan1_price = store[divan_code][0]['price']
divan1_cost = divan1_quantity * divan1_price

divan2_quantity = store[divan_code][1]['quantity']
divan2_price = store[divan_code][1]['price']
divan2_cost = divan2_quantity * divan2_price

divan_total_quantity = divan1_quantity + divan2_quantity
divan_total_cost = divan1_cost + divan2_cost
print(f'Диван - {divan_total_quantity} шт, стоимость {divan_total_cost} руб')

stul_code = goods['Стул']

stul1_quantity = store[stul_code][0]['quantity']
stul1_price = store[stul_code][0]['price']
stul1_cost = stul1_quantity * stul1_price

stul2_quantity = store[stul_code][1]['quantity']
stul2_price = store[stul_code][1]['price']
stul2_cost = stul2_quantity * stul2_price

stul3_quantity = store[stul_code][2]['quantity']
stul3_price = store[stul_code][2]['price']
stul3_cost = stul3_quantity * stul3_price

stul_total_quantity = stul1_quantity + stul2_quantity + stul3_quantity
stul_total_cost = stul1_cost + stul2_cost + stul3_cost
print(f'Стул - {stul_total_quantity} шт, стоимость {stul_total_cost} руб')