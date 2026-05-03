#!/usr/bin/env python3
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [{'quantity': 27, 'price': 42}],
    '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}],
    '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
    '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}],
}

def calculate_product_cost(product_name):
    code = goods[product_name]
    items = store[code]
    total_quantity = 0
    total_cost = 0
    for item in items:
        total_quantity += item['quantity']
        total_cost += item['quantity'] * item['price']
    return total_quantity, total_cost

def get_all_products_cost():
    results = {}
    for product in goods.keys():
        quantity, cost = calculate_product_cost(product)
        results[product] = {'quantity': quantity, 'cost': cost}
    return results

if __name__ == "__main__":
    for product, data in get_all_products_cost().items():
        print(f'{product} - {data["quantity"]} шт, стоимость {data["cost"]} руб')