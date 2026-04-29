import math

def root_iterative(n):
    if n < 1:
        return None
    
    result = math.sqrt(3)  # для n = 1
    
    for i in range(2, n + 1):
        result = math.sqrt(3 + result)
    
    return result

def main():
    try:
        n = int(input('введите количество корней n: '))
        if n < 1:
            print('n должно быть >= 1')
            return
        
        result = root_iterative(n)
        print(f'x_{n} = {result}')
        
    except ValueError:
        print('Ошибка: введите целое число')

if __name__ == "__main__":
    main()