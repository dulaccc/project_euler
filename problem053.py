#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 53
#
# There are exactly ten ways of selecting three from five, 12345:
#
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
# In combinatorics, we use the notation, 5C3 = 10.
#
# In general,
#
# nCr = n! / r!(nr)!  where r  n, n! = n(n1)...321, and 0! = 1.
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?

import time
import math

t = time.time()

def comb(r,n):
  return math.factorial(n) / (math.factorial(r)*math.factorial(n-r))

s = 0
for n in range(1,100+1):
  for r in range(1,n+1):
    if comb(r,n) > 1e6:
      s += 1

print s
print "time: %f s" % (time.time() - t)