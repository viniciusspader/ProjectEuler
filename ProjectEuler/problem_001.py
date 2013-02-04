"""
Problem Description
-------------------
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from sys import *

print """
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below number x.
"""

limit = int(raw_input("Which value x is? "))
solution = 0

for n in range(1, limit):
    if n % 3 == 0 or n % 5 == 0:
        solution += n
    else:
        pass

print "The solution is: %d." % solution
