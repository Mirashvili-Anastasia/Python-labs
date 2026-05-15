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

print(fib())
print(fib())
print(fib())
print(fib())
print(fib())
print(fib())
print(fib())
print(fib())