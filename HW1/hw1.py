# Name: Jessica Morton
# Evergreen Login: morjes14
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                # makes the math.sqrt function available
import hw1_test            # makes the variables within hw1_test available

from hw1_test import *        # creates bindings in current scope to
                              # to all objects defined within hw1_test

###
### Problem 1
###

print "Problem 1 solution follows:"

# Roots of the quadratic equation ax^2+bx+c are:
# b+sqrt(b^2 - 4 * a * c)/2 * 1 and 
# b-sqrt(b^2 - 4 * a * c)/2 * 1

x1 = (5.86+math.sqrt(5.86**2-4*1*8.5408))/2*1
x2 = (5.86-math.sqrt(5.86**2-4*1*8.5408))/2*1

print #line of whitespace
print "The square root of the quadratic equation x^2-5.86x+8.5408 is:"
print "x1 =", x1, "x2 =", x2
print #line of whitespace

###
### Problem 2
###

print "Problem 2 solution follows:"

print #line of whitespace
print "a =", str(a)            # converts bool to str and prints value
print "b =", str(b)
print "c =", str(c)
print "d =", str(d)
print "e =", str(e)
print "f =", str(f)
print #line of whitespace

###
### Problem 3
###

print "Problem 3 solution follows:"

print #line of whitespace
print "((a and b) or (not c) and not (d or e or f)) ="
print str(((a and b) or (not c) and not (d or e or f)))

###
### Collaboration
###

# None