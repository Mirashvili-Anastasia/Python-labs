def cache_decorator(func):
    memory = {}

    def wrapper(*args, **kwargs):

        key = (args, tuple(sorted(kwargs.items())))

        if key in memory:
            print(f"Беру из кэша для {key}")
            return memory[key]

        print(f"Вычисляю впервые для {key}")
        result = func(*args, **kwargs)

        memory[key] = result

        return result

    return wrapper

@cache_decorator
def slow_multiply(x, y):
    import time
    time.sleep(2)
    return x * y


print(slow_multiply(3, 4))
print(slow_multiply(3, 4))
print(slow_multiply(5, 2))
print(slow_multiply(3, 4))