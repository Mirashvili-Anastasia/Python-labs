#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Lyudmila', 'Denis', 'Nastya', 'Sergey']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    ['Lyudmila', 162],
    ['Denis', 177],
    ['Nastya', 160],
    ['Sergey', 177]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост отца - {my_family_height[3][1]} см')

total_height = 0
for person in my_family_height:
    total_height = total_height + person[1]

print(f"Общий рост моей семьи - {total_height} см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
