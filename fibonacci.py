import math

def sum_even(maximum):
    n, n_1, n_2 = 1, 1, 0
    sum_n = 0
    while(sum_n < maximum):
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n
        if (n % 2 == 0):
            sum_n = sum_n + n
    return sum_n


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def prime_factors(num):
    number = num
    divisor = 2
    factors = []
    while True:
        if is_prime(divisor):
            rem = number % divisor
            if rem == 0:
                number = number / divisor
                factors.append(divisor)
        divisor = divisor + 1
        if divisor > math.sqrt(num):
            break

    return factors


def factorial(num):
    r = 1
    for num_r in range(1, num + 1):
        r = r * num_r
    return r


def combinations(num1, num2):
    r = factorial(num1)
    r1 = factorial(num2)
    r3 = factorial(num1 - num2)
    return factorial(num1) / (factorial(num2) * factorial(num1 - num2))


def permutations(num1, num2):
    return factorial(num1) / factorial(num2)


print(sum_even(4000000))
print(prime_factors(600851475143))
print("Combinations ", combinations(40, 20))
print(factorial(10))
print(factorial(5))
print(factorial(6))
print(combinations(4, 2))
print(combinations(6, 3))
print(combinations(7, 3))
print(combinations(7, 4))


def choices(matrix, size):
    for i in range(0, size + 1):
        matrix[i][size] = 1
        matrix[size][i] = 1
    for i in range(size - 1, -1, -1):
        for j in range(size - 1, -1, -1):
            matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]
    return matrix[0][0]


size = 20
matrix = [[0 for i in range(size + 1)] for i in range(size + 1)]
print(choices(matrix, size))



