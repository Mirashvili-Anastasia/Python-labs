def find_numbers_with_divisor_ending_8():
    results = []
    num = 500001
    
    while len(results) < 5:
        divisors_ending_8 = []
        
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:
                if i % 10 == 8 and i != 8 and i != num:
                    divisors_ending_8.append(i)
                j = num // i
                if j != i and j % 10 == 8 and j != 8 and j != num:
                    divisors_ending_8.append(j)
        
        if divisors_ending_8:
            min_divisor = min(divisors_ending_8)
            results.append((num, min_divisor))
        
        num += 1
    
    return results

if __name__ == "__main__":
    numbers = find_numbers_with_divisor_ending_8()
    for number, divisor in numbers:
        print(number, divisor)