#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_family = ['Lyudmila', 'Denis', 'Nastya', 'Sergey']

my_family_height = [
    ['Lyudmila', 162],
    ['Denis', 177],
    ['Nastya', 160],
    ['Sergey', 177]
]

def get_father_height():
    return my_family_height[3][1]

def get_total_family_height():
    total = 0
    for person in my_family_height:
        total += person[1]
    return total

if __name__ == "__main__":
    print(f'Рост отца - {get_father_height()} см')
    print(f"Общий рост моей семьи - {get_total_family_height()} см")