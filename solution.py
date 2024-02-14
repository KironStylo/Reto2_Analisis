import functools


def problem_1(n):
    suma: int = 0
    for num in range(n - 1):
        if (num + 1) % 3 == 0 or (num + 1) % 5 == 0:
            suma += num + 1
    return suma


def fib_to(n):
    fibs = [1, 2]
    for i in range(2, n + 1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def problem_2(n):
    fib = fib_to(n - 1)
    pares = list(filter(lambda x: x % 2 == 0, fib))
    suma = functools.reduce((lambda x, y: x + y), pares)
    return suma


def prime_factor(n):
    factores = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factores.append(divisor)
            n /= divisor
        divisor += 1
    return factores


def find_largest_palindrome_product():
    largest_palindrome = 0
    for i in range(100, 1000):
        for u in range(i + 1, 1000):
            if str(i * u) == str(i * u)[::-1]:
                largest_palindrome = i * u
    return largest_palindrome


def smallest_multiple(n):
    found = False
    number = 1
    while not found:
        found2 = True
        for i in range(1, n + 1):
            if number % i != 0:
                found2 = False
            if not found2:
                break
        if found2:
            return number
        number += 1
    print(number)
    return number


def problem_5(n):
    return smallest_multiple(n)


def problem_4():
    return find_largest_palindrome_product()


def problem_3(n):
    return max(prime_factor(n))