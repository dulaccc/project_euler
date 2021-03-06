#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# The Euler Project: problem 44
#
# Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. 
# The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their 
# difference, 70 - 22 = 48, is not pentagonal.
#
# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
# difference is pentagonal and D = |Pk - Pj| is minimised; what is the value of D?

import math
import time

def pentagonal(n):
  return int(1.0*n*(3*n-1)/2)

t = time.time()

# brute force (ne converge pas)
# pent = []
# for n in range(1,10**4):
#   p = pentagonal(n)
#   for pp in pent:
#     if (pp+p) in pent and (pp-p) in pent:
#       print "Found"
#     print n,p
#   pent.append(p)

# Pi + Pj = Pk1
# Pi - Pj = Pk2
# resolve this equations (with i>j and k1>k2 and k1>i and i>k2)
couple = None
for k1 in xrange(1,10**4):
  for k2 in xrange(1,k1):
    #print k1,k2
    i = ( 1. + math.sqrt(1+6*(k1*(3*k1-1) + k2*(3*k2-1))) ) / 6
    if i <= 0 or int(i) != i: continue
    j = ( 1. + math.sqrt(1+6*(k1*(3*k1-1) - k2*(3*k2-1))) ) / 6
    if j <= 0 or int(j) != j: continue
      
    couple = (i,j,k1,k2)
    break
  if couple:
    break

i,j = couple[:2]
print "end"
print "couple: ", couple
print "Pi", pentagonal(i)
print "Pj", pentagonal(j)
print "D = |Pi - Pj| =", pentagonal(i) - pentagonal(j)
print "time: %f s" % (time.time() - t)