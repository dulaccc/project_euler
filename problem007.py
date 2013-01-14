#!/usr/bin/env python
#
# The Euler Project: problem 7
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from prime import *

i = 0
for p in prime(limit=1e6):
  i += 1
  if i == 10001:
    break

print i, p