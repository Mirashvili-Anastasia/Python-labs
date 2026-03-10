s = 5**36 + 5**24 - 25
def count_combo():
    count = 0
    n = s
    while n > 0:
        if n % 5 == 4:
            count += 1
        n = n // 5
    return count
result = count_combo()
print(result)
