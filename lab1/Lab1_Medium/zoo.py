#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def process_zoo():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    birds = ['rooster', 'ostrich', 'lark']

    # Вставка медведя
    zoo.insert(1, 'bear')

    # Добавление птиц
    zoo.extend(birds)

    # Удаление слона
    zoo.remove('elephant')

    # Поиск индексов
    lion_index = zoo.index('lion')
    lark_index = zoo.index('lark')

    return {
        'final_zoo': zoo,
        'lion_position': lion_index + 1,
        'lark_position': lark_index + 1
    }


if __name__ == "__main__":
    result = process_zoo()
    print(result['final_zoo'])
    print(f'Лев в: {result["lion_position"]}')
    print(f'Жаворонок в: {result["lark_position"]}')