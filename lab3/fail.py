from itertools import product
def count_combo():
    letters = ('Г', 'Е', 'П', 'А', 'Р', 'Д')
    count = 0
    for combo in product(letters, repeat = 6):
        word = list(combo)
        if word.count('Г') == 1 and word[0] != 'А' and word[4] != 'Е':
            count += 1
    return count
result = count_combo()
print(result)