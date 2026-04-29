import math

def root(n):
    if n == 1:
        return math.sqrt(3)
    else:
        return math.sqrt(3 + root(n-1))
def main():
    try:
        n = int(input('введите количество корней n: '))
        if n < 2:
            print('n должно быть >= 1')
            return
        result = root(n)
        print(f'x_{n} = {result}')
    except ValueError:
        print('Ошибка: введите целое число')

if __name__ == "__main__":
    main()