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

    # One itself is a prime number, but not for the purpose of this problem
    if n == 1:
        return False

    # Prime numbers that will be chatch on the tests
    elif n in [2, 3, 5]:
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


def find_prime_factors(n):
    # Store the quotient of the division by the prime factors
    remaining = n

    # Initiate a variable to store the factors
    factors = []

    # Start i (counter) as 2, because is the first prime factor to be used
    i = 2

    # Iterates from 2 to the number specified to find the prime factors
    # Stops when it finds all the prime factors (remaining = 1)

    # I used break just above, but I don't understand why it does not evaluate
    # it here
    while i <= n or remaining == 1:
        if is_prime(i):
            while remaining % i == 0:
                factors.append(i)
                remaining /= i
        else:
            pass

        i += 1
        
        # I'm using it here because it seems not to evaluate on while clause
        if remaining == 1:
            break
        else:
            pass

    return factors

def return_largest_prime_factor(n):
    prime_factors = find_prime_factors(n)
    return max(prime_factors)