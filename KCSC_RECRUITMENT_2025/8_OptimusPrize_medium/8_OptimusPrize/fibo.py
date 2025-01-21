def fibonacci(n):
    fib_list = [0, 0x1] 
    for i in range(2, n): 
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        next_fib &= 0xFFFFFFFF
        fib_list.append(next_fib)
    return fib_list

n = 100  
fib_numbers = fibonacci(n)

for i in range(len(fib_numbers)):
    if i % 10 == 9: print(f'0x{fib_numbers[i]:08X}', end = ',\n')
    else: print(f'0x{fib_numbers[i]:08X}', end = ', ')

