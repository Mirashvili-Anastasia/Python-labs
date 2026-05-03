#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

def calculate_distance(city1, city2, sites_dict=None):
    if sites_dict is None:
        sites_dict = sites
    x1, y1 = sites_dict[city1]
    x2, y2 = sites_dict[city2]
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return round(distance, 2)

def build_distances_matrix(sites_dict=None):
    if sites_dict is None:
        sites_dict = sites
    distances = {}
    cities = list(sites_dict.keys())
    for city1 in cities:
        distances[city1] = {}
        for city2 in cities:
            if city1 != city2:
                distances[city1][city2] = calculate_distance(city1, city2, sites_dict)
    return distances

if __name__ == "__main__":
    print(build_distances_matrix())