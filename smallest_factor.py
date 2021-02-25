#! /usr/bin/env python3

# A script for getting the smallest prime factor of an integer.

import sys

if len(sys.argv) != 2:
    sys.exit(sys.argv[0] + ": Expecting one command line argument -- the integer for which to get the smallest factor")
n = int(sys.argv[1])
if n < 1:
    sys.exit(sys.argv[0] + ": Expecting a positive integer")

def smallest_prime_factor(n):
    for i in range(2, n):
        if (n % i) == 0:
            return i
    return none

if smallest_prime_factor is None:
    print(n)
else:
    print(smallest_prime_factor)
