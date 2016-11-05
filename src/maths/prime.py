
""" Primes
A number is prime if it is only divisible by 1 and itself. 
So for example 2, 3, 5, 79, 311 and 1931 are all prime, 
while 21 is not prime because it is divisible by 3 and 7 """
__author__ = "AmrReda"

from math import *

def isPrime(n):
    if n <= 1: 
        return False
    if n == 2: 
        return True
    
    m = sqrt(n)

    for i in range(3, m):
        if n % i == 0:
            return False
        i += 2

    return True

x = int(raw_input("Please enter a number:"))
print isPrime(5)