#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import radians

def calculate_circle_area(radius, pi=3.1415926):
    return round(pi * radius ** 2, 4)

def is_point_inside_circle(point, radius, center=(0, 0)):
    x, y = point
    cx, cy = center
    distance = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
    return distance <= radius

if __name__ == "__main__":
    radius = 42
    print(calculate_circle_area(radius))
    print(is_point_inside_circle((23, 34), radius))
    print(is_point_inside_circle((30, 30), radius))