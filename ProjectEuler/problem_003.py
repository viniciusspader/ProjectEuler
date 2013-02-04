"""
Problem Description
-------------------
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def sum_digits(n):
    total = 0

    for x in str(n):
        total += int(x)

    return total


def is_prime(n):

    # Prime numbers that will be chatch on the tests
    if n in [1, 2, 3, 5]:
        return True

    # Check if the number is even
    elif n % 2 == 0:
        return False

    # Check if the sum of the digits is divisible by 3
    elif sum_digits(n) % 3 == 0:
        return False

    # Check if the last two digits are divisible by 4
    elif (n % 100) % 4 == 0:
        return False

    # Check if the last number is 0 or 5
    elif n % 10 in [0, 5]:
        return False

    else:
        return True

def create_prime_list(n):
    prime_list = []

    for x in range(n + 1):
        if is_prime(x):
            prime_list.append(x)

    return prime_list

def find_prime_factors(n):
    primes = create_prime_list(n)