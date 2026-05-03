#!/usr/bin/env python3
# -*- coding: utf-8 -*-

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

def get_garden_set():
    return set(garden)

def get_meadow_set():
    return set(meadow)

def get_all_flowers():
    return get_garden_set() | get_meadow_set()

def get_common_flowers():
    return get_garden_set() & get_meadow_set()

def get_only_garden():
    return get_garden_set() - get_meadow_set()

def get_only_meadow():
    return get_meadow_set() - get_garden_set()

if __name__ == "__main__":
    print(get_all_flowers())
    print(get_common_flowers())
    print(get_only_garden())
    print(get_only_meadow())