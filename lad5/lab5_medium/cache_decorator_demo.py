import time
from functools import wraps


def cache_decorator(maxsize=None, logging_enabled=True):
    """
    Декоратор для кэширования результатов с опциональными параметрами.

    Параметры:
    - maxsize: максимальный размер кэша (None = безлимитный, число = ограниченный LRU)
    - logging_enabled: включить/выключить логирование (True/False)
    """

    def decorator(func):
        memory = {}
        cache_hits = 0
        cache_misses = 0
        recursion_depth = 0  # Для поддержки рекурсивных функций

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal cache_hits, cache_misses, recursion_depth

            # Увеличиваем глубину рекурсии
            recursion_depth += 1
            indent = "  " * (recursion_depth - 1)  # Отступ для визуализации

            # Создаем ключ из аргументов
            key = (args, tuple(sorted(kwargs.items())))

            # Логирование входа в функцию
            if logging_enabled:
                current_time = time.strftime("%H:%M:%S")
                # Формируем строку с аргументами
                args_list = []
                for arg in args:
                    args_list.append(str(arg))
                for k, v in kwargs.items():
                    args_list.append(f"{k}={v}")
                args_str = f"({', '.join(args_list)})" if args_list else "(нет аргументов)"

                print(f"{indent}[{current_time}] Вызвана {func.__name__}{args_str}")

            # Проверка кэша
            start_time = time.time() if logging_enabled else None

            if key in memory:
                cache_hits += 1
                if logging_enabled:
                    elapsed_ms = (time.time() - start_time) * 1000 if start_time else 0
                    print(f"{indent}[{time.strftime('%H:%M:%S')}] ВЗЯТО ИЗ КЭША! (хит #{cache_hits})")
                    print(f"{indent}[{time.strftime('%H:%M:%S')}] Вернула: {memory[key]} [{elapsed_ms:.2f} мс]")

                # Уменьшаем глубину рекурсии
                recursion_depth -= 1
                if recursion_depth == 0 and logging_enabled:
                    print(f"{indent}{'-' * 50}")

                return memory[key]

            # Если нет в кэше - вычисляем
            cache_misses += 1
            if logging_enabled:
                print(f"{indent}[{time.strftime('%H:%M:%S')}] ВЫЧИСЛЯЮ ВПЕРВЫЕ (промах #{cache_misses})")

            # Вызываем оригинальную функцию (поддерживает рекурсию)
            result = func(*args, **kwargs)

            # Сохраняем в кэш
            memory[key] = result

            # LRU: если превышен лимит, удаляем самый старый элемент
            if maxsize is not None and len(memory) > maxsize:
                oldest_key = next(iter(memory))
                del memory[oldest_key]
                if logging_enabled:
                    print(
                        f"{indent}[{time.strftime('%H:%M:%S')}]  Превышен лимит кэша ({maxsize}), удалён {oldest_key}")

            # Логирование выхода
            if logging_enabled:
                elapsed_ms = (time.time() - start_time) * 1000 if start_time else 0
                print(f"{indent}[{time.strftime('%H:%M:%S')}] Вернула: {result} [{elapsed_ms:.2f} мс]")

            # Уменьшаем глубину рекурсии
            recursion_depth -= 1

            # Разделитель после первого вызова
            if recursion_depth == 0 and logging_enabled:
                print(f"{indent}{'-' * 50}")

            return result

        # Добавляем полезные методы
        def cache_info():
            return {
                'size': len(memory),
                'maxsize': maxsize,
                'hits': cache_hits,
                'misses': cache_misses,
                'hit_ratio': cache_hits / (cache_hits + cache_misses) if (cache_hits + cache_misses) > 0 else 0
            }

        def cache_clear():
            nonlocal cache_hits, cache_misses
            memory.clear()
            cache_hits = 0
            cache_misses = 0
            if logging_enabled:
                print("[КЭШ] Очищен")

        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    # Поддержка использования без параметров и с параметрами
    if callable(maxsize):
        # @cache_decorator (без скобок)
        func = maxsize
        maxsize = None
        return decorator(func)

    # @cache_decorator() или @cache_decorator(maxsize=5, logging_enabled=False)
    return decorator


# ============== ПЕРВАЯ ПРОГРАММА (Фибоначчи) ==============
print("=" * 60)
print("ЗАДАЧА 1: Генератор Фибоначчи (без кэша)")
print("=" * 60)


def fibonacci_closure():
    a = 0
    b = 1

    def get_next():
        nonlocal a, b
        result = a
        a, b = b, a + b
        return result

    return get_next


fib = fibonacci_closure()

print("Первые 8 чисел Фибоначчи:")
for i in range(8):
    print(f"fib({i}) = {fib()}")

# ============== ВТОРАЯ ПРОГРАММА (с декоратором) ==============
print("\n" + "=" * 60)
print("ЗАДАЧА 2: Декоратор с кэшем для slow_multiply")
print("=" * 60)


@cache_decorator(logging_enabled=True)
def slow_multiply(x, y):
    """Медленное умножение с задержкой"""
    import time
    time.sleep(1)  # Уменьшил до 1 секунды для демонстрации
    return x * y


print("Вызовы slow_multiply:")
print(f"3 * 4 = {slow_multiply(3, 4)}")
print(f"3 * 4 = {slow_multiply(3, 4)}")  # Из кэша
print(f"5 * 2 = {slow_multiply(5, 2)}")
print(f"3 * 4 = {slow_multiply(3, 4)}")  # Из кэша

print(f"\nСтатистика кэша: {slow_multiply.cache_info()}")

# ============== ПОДДЕРЖКА РЕКУРСИВНЫХ ФУНКЦИЙ ==============
print("\n" + "=" * 60)
print("ЗАДАЧА 3: Рекурсивное вычисление факториала с кэшем")
print("=" * 60)


@cache_decorator(maxsize=10, logging_enabled=True)
def factorial(n):
    """Вычисление факториала рекурсивно"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print("Вычисление факториалов:")
print(f"5! = {factorial(5)}")
print(f"5! = {factorial(5)}")  # Из кэша
print(f"7! = {factorial(7)}")  # Частично из кэша
print(f"Статистика: {factorial.cache_info()}")

# ============== РЕКУРСИВНОЕ ФИБОНАЧЧИ С КЭШЕМ ==============
print("\n" + "=" * 60)
print("ЗАДАЧА 4: Рекурсивное Фибоначчи (классическая рекурсия)")
print("=" * 60)


@cache_decorator(maxsize=None, logging_enabled=True)
def fib_recursive(n):
    """Рекурсивное вычисление чисел Фибоначчи с кэшем"""
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


print("Рекурсивное вычисление fib(6):")
print(f"fib(6) = {fib_recursive(6)}")
print(f"fib(6) = {fib_recursive(6)}")  # Мгновенно из кэша
print(f"fib(10) = {fib_recursive(10)}")  # Использует кэш от предыдущих вычислений

print(f"\nИтоговая статистика: {fib_recursive.cache_info()}")

# ============== РАЗЛИЧНЫЕ ВАРИАНТЫ ИСПОЛЬЗОВАНИЯ ==============
print("\n" + "=" * 60)
print("ЗАДАЧА 5: Различные варианты использования декоратора")
print("=" * 60)


# Вариант 1: Без параметров (безлимитный кэш)
@cache_decorator
def add(a, b):
    return a + b


# Вариант 2: С ограничением кэша
@cache_decorator(maxsize=2)
def multiply(a, b):
    return a * b


# Вариант 3: Без логирования
@cache_decorator(logging_enabled=False)
def fast_square(x):
    return x * x


# Вариант 4: С ограничением и без логирования
@cache_decorator(maxsize=3, logging_enabled=False)
def power(base, exp):
    return base ** exp


print("Тестирование разных вариантов:")
print(f"add(5,3) = {add(5, 3)}")
print(f"add(5,3) = {add(5, 3)} (из кэша)")
print(f"multiply(4,5) = {multiply(4, 5)}")
print(f"fast_square(10) = {fast_square(10)}")
print(f"power(2,10) = {power(2, 10)}")

# ============== СРАВНЕНИЕ С ВАШИМ ОРИГИНАЛЬНЫМ КОДОМ ==============
print("\n" + "=" * 60)
print("ЗАДАЧА 6: Исправленный вариант кода")
print("=" * 60)


# Исправленный вариант вашего декоратора (без ошибок)
def simple_cache_decorator(func):
    memory = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in memory:
            print(f"Беру из кэша для {key}")
            return memory[key]

        print(f"Вычисляю впервые для {key}")
        result = func(*args, **kwargs)
        memory[key] = result  # <-- ИСПРАВЛЕНО: сохраняем результат

        return result

    return wrapper


@simple_cache_decorator
def corrected_slow_multiply(x, y):
    import time
    time.sleep(1)
    return x * y


print("Исправленная версия:")
print(f"3 * 4 = {corrected_slow_multiply(3, 4)}")
print(f"3 * 4 = {corrected_slow_multiply(3, 4)}")
print(f"5 * 2 = {corrected_slow_multiply(5, 2)}")
print(f"3 * 4 = {corrected_slow_multiply(3, 4)}")

# ============== ОЧИСТКА КЭША ==============
print("\n" + "=" * 60)
print("ДОПОЛНИТЕЛЬНО: Очистка кэша")
print("=" * 60)


@cache_decorator(maxsize=2, logging_enabled=True)
def demo_clear(x):
    return x * 10


print("До очистки:")
demo_clear(1)
demo_clear(2)
print(f"Статистика: {demo_clear.cache_info()}")

print("\nОчищаем кэш:")
demo_clear.cache_clear()

print("\nПосле очистки:")
demo_clear(1)  # Снова вычисляется
print(f"Статистика: {demo_clear.cache_info()}")