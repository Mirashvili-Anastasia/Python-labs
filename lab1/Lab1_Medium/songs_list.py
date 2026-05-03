#!/usr/bin/env python3
# -*- coding: utf-8 -*-

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

def get_three_songs_time(songs_list, song_names):
    total = 0
    for song_name in song_names:
        for song in songs_list:
            if song[0] == song_name:
                total += song[1]
                break
    return round(total, 2)

def get_first_three_total():
    return get_three_songs_time(violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean'])

def get_second_three_total():
    return get_three_songs_time(violator_songs_list, ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress'])

if __name__ == "__main__":
    print(f"Три песни звучат {get_first_three_total()} минут")
    print(f"А другие три песни звучат {get_second_three_total()} минут")