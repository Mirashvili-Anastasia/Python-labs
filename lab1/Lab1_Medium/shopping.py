#!/usr/bin/env python3
# -*- coding: utf-8 -*-

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}


def get_best_prices():
    sweets = {}
    products = ['печенье', 'конфеты', 'карамель', 'пирожное']

    for product in products:
        prices = []
        for shop_name, items in shops.items():
            for item in items:
                if item['name'] == product:
                    prices.append({'shop': shop_name, 'price': item['price']})
        # Сортируем по цене и берем 2 самых дешевых
        prices.sort(key=lambda x: x['price'])
        sweets[product] = prices[:2]

    return sweets


if __name__ == "__main__":
    print(get_best_prices())