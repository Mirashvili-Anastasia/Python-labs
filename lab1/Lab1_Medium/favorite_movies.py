#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

def get_first_movie():
    return my_favorite_movies[:10]

def get_last_movie():
    return my_favorite_movies[42:57]

def get_second_movie():
    return my_favorite_movies[12:25]

def get_second_from_end():
    return my_favorite_movies[35:40]

def get_all_movies():
    return {
        'first': get_first_movie(),
        'last': get_last_movie(),
        'second': get_second_movie(),
        'second_from_end': get_second_from_end()
    }

if __name__ == "__main__":
    print(get_first_movie())
    print(get_last_movie())
    print(get_second_movie())
    print(get_second_from_end())