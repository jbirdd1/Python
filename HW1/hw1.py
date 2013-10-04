# Name: Jessica Morton
# Evergreen Login: morjes14
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                    # makes the math.sqrt function available
import hw1_test                # makes the variables within hw1_test available
                                # have to use 'hw1_test.a' instead of just 'a'

from math import *            # imports everything from math module so 'sqrt' 
                                # can be used instead of 'math.sqrt'

from hw1_test import *        # imports everything from hw1_test module so just 
                                # 'a' can be used instead of 'hw_test.a'

###
### Problem 1
###

print "Problem 1 solution follows:"

# Roots of the quadratic equation ax^2+bx+c are:
# b+sqrt(b^2 - 4 * a * c)/2 * 1 and 
# b-sqrt(b^2 - 4 * a * c)/2 * 1

x1 = (5.86+sqrt(5.86**2-4*1*8.5408))/2*1
x2 = (5.86-sqrt(5.86**2-4*1*8.5408))/2*1

print #line of whitespace
print "The square root of the quadratic equation x^2-5.86x+8.5408 is:"
print "x1 =", x1, "x2 =", x2
print #line of whitespace

###
### Problem 2
###

print "Problem 2 solution follows:"

print #line of whitespace
print "a =", str(hw1_test.a)            # converts bool to str and prints value
print "b =", str(hw1_test.b)
print "c =", str(hw1_test.c)
print "d =", str(hw1_test.d)
print "e =", str(hw1_test.e)
print "f =", str(hw1_test.f)
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

# ... List your collaborators here, as a comment (on a line starting with "#").
