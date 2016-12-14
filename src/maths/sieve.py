"""
Sieve of Eratosthenes is a prime number generator algorithm
"""
__author__ = "AmrReda"


def sieve(number):
    not_prime = []
    for i in xrange(2, number + 1):
        if i not in not_prime:
            print i
            for j in xrange(i * i, number + 1, i):
                not_prime.append(j)

sieve(100)
