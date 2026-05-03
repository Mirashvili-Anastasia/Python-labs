#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Верхнеуровневый модуль для лабораторной работы №1
Интерактивный режим: вывод только выбранных программ
"""

import distance
import circle
import operations
import favorite_movies
import my_family
import zoo
import songs_list
import secret
import garden
import shopping
import store


def show_menu():
    """Показывает меню со списком программ"""
    print("\n" + "=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №1")
    print("=" * 60)
    print("Доступные программы:")
    print("  1 - Расстояния между городами")
    print("  2 - Круг и точки")
    print("  3 - Арифметическое выражение")
    print("  4 - Любимые фильмы")
    print("  5 - Моя семья")
    print("  6 - Зоопарк")
    print("  7 - Песни Depeche Mode")
    print("  8 - Зашифрованное сообщение")
    print("  9 - Цветы в саду и на лугу")
    print("  10 - Магазины сладостей")
    print("  11 - Склад товаров")
    print("  all - Выполнить все программы")
    print("  exit - Выход")
    print("-" * 60)


def run_program(choice):
    """Запускает выбранную программу"""

    if choice == "1":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 1: РАССТОЯНИЯ МЕЖДУ ГОРОДАМИ")
        print("=" * 60)
        distances = distance.build_distances_matrix()
        for city, destinations in distances.items():
            for dest, dist in destinations.items():
                print(f"  {city} → {dest}: {dist}")
        print("-" * 60)

    elif choice == "2":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 2: КРУГ И ТОЧКИ")
        print("=" * 60)
        radius = 42
        print(f"  Площадь круга (r={radius}): {circle.calculate_circle_area(radius)}")
        point1, point2 = (23, 34), (30, 30)
        print(f"  Точка {point1} внутри круга: {circle.is_point_inside_circle(point1, radius)}")
        print(f"  Точка {point2} внутри круга: {circle.is_point_inside_circle(point2, radius)}")
        print("-" * 60)

    elif choice == "3":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 3: АРИФМЕТИЧЕСКОЕ ВЫРАЖЕНИЕ")
        print("=" * 60)
        print(f"  (1*2+3)*4+5 = {operations.calculate_expression()}")
        print("-" * 60)

    elif choice == "4":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 4: ЛЮБИМЫЕ ФИЛЬМЫ")
        print("=" * 60)
        movies = favorite_movies.get_all_movies()
        print(f"  Первый фильм: {movies['first']}")
        print(f"  Второй фильм: {movies['second']}")
        print(f"  Второй с конца: {movies['second_from_end']}")
        print(f"  Последний фильм: {movies['last']}")
        print("-" * 60)

    elif choice == "5":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 5: МОЯ СЕМЬЯ")
        print("=" * 60)
        print(f"  Рост отца: {my_family.get_father_height()} см")
        print(f"  Общий рост семьи: {my_family.get_total_family_height()} см")
        print("-" * 60)

    elif choice == "6":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 6: ЗООПАРК")
        print("=" * 60)
        zoo_result = zoo.process_zoo()
        print(f"  Финальный список животных: {zoo_result['final_zoo']}")
        print(f"  Лев в клетке №{zoo_result['lion_position']}")
        print(f"  Жаворонок в клетке №{zoo_result['lark_position']}")
        print("-" * 60)

    elif choice == "7":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 7: ПЕСНИ DEPECHE MODE")
        print("=" * 60)
        print(f"  Три песни звучат: {songs_list.get_first_three_total()} минут")
        print(f"  А другие три песни звучат: {songs_list.get_second_three_total()} минут")
        print("-" * 60)

    elif choice == "8":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 8: ЗАШИФРОВАННОЕ СООБЩЕНИЕ")
        print("=" * 60)
        print(f"  Расшифрованное сообщение: {secret.decrypt_message()}")
        print("-" * 60)

    elif choice == "9":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 9: ЦВЕТЫ В САДУ И НА ЛУГУ")
        print("=" * 60)
        print(f"  Все цветы: {garden.get_all_flowers()}")
        print(f"  Цветы, растущие и там, и там: {garden.get_common_flowers()}")
        print(f"  Цветы только в саду: {garden.get_only_garden()}")
        print(f"  Цветы только на лугу: {garden.get_only_meadow()}")
        print("-" * 60)

    elif choice == "10":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 10: МАГАЗИНЫ СЛАДОСТЕЙ")
        print("=" * 60)
        best_prices = shopping.get_best_prices()
        for product, shops_list in best_prices.items():
            print(f"  {product}:")
            for shop_info in shops_list:
                print(f"    - {shop_info['shop']}: {shop_info['price']} руб")
        print("-" * 60)

    elif choice == "11":
        print("\n" + "=" * 60)
        print("ПРОГРАММА 11: СКЛАД ТОВАРОВ")
        print("=" * 60)
        all_products = store.get_all_products_cost()
        for product, data in all_products.items():
            print(f"  {product}: {data['quantity']} шт, стоимость {data['cost']} руб")
        print("-" * 60)

    elif choice == "all":
        print("\n" + "=" * 60)
        print("ВЫПОЛНЕНИЕ ВСЕХ ПРОГРАММ")
        print("=" * 60)
        for i in range(1, 12):
            run_program(str(i))

    elif choice == "exit":
        print("\nДо свидания!")
        return False

    else:
        print("\nНеверный выбор! Пожалуйста, введите номер программы (1-11), 'all' или 'exit'")

    return True


def main():
    """Главная функция программы"""
    while True:
        show_menu()
        user_choice = input("Введите номер программы: ").strip().lower()

        if not run_program(user_choice):
            break


if __name__ == "__main__":
    main()