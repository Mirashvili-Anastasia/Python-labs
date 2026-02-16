#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = []

Moscow_distances_London = round(((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1] ** 2)) ** 0.5)
Moscow_distances_Paris = round(((sites['Moscow'][0] - sites['Paris'][0]) ** 2 + (sites['Moscow'][1] - sites['Paris'][1] ** 2)) ** 0.5)

London_distances_Moscow = round(((sites['London'][0] - sites['Moscow'][0]) ** 2 + (sites['London'][1] - sites['Moscow'][1] ** 2)) ** 0.5)
London_distances_Paris = round(((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1] ** 2)) ** 0.5)

Paris_distances_Moscow = round(((sites['Paris'][0] - sites['Moscow'][0]) ** 2 + (sites['Paris'][1] - sites['Moscow'][1] ** 2)) ** 0.5)
Paris_distances_London = round(((sites['Paris'][0] - sites['London'][0]) ** 2 + (sites['Paris'][1] - sites['London'][1] ** 2)) ** 0.5)

distances['Moscow'] = {
    'London': Moscow_distances_London
    'Paris': Moscow_distances_Paris
}

distances['London'] = {
    'Moscow': London_distances_Moscow
    'Paris': London_distances_Paris
}

distances['Paris'] = {
    'London': Paris_distances_Londo
    'Moscow': Paris_distances_Moscow
}


# TODO здесь заполнение словаря

print(distances)




