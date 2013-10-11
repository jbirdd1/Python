# Name: Jessica Morton
# Evergreen Login: morjes14
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

from hw2_test import * 
import itertools

###
### Problem 1
###

### DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"
print #line of whitespace

total = 0
x = 0
while (x < n):
# runs through numbers 0 - 10 and adds the total + (value of x + 1) each time
    total = total + (x + 1)
    x = x + 1
    # adds 1 to the value of x after each iteration
    
print "The Sum of 1 to %d " %n + "= %d" %total
    
print #line of whitespace

###
### Problem 2
###

### DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"
print #line of whitespace

fractionList = ['1/2', '1/3', '1/4', '1/5', '1/6', '1/7', '1/8', '1/9', '1/10']
decimalList = [1.0/2, 1.0/3, 1.0/4, 1.0/5, 1.0/6, 1.0/7, 1.0/8, 1.0/9, 1.0/10]
# decimalList computes each fraction into decimal by simply dividing the nubmers

for fraction, decimal in itertools.izip(fractionList, decimalList):
# for loop with 2 conditions using the library 'itertools' so numbers from both 
# lists can be printed on same line
    print "%s =" %fraction + " %s " %decimal
    
print #line of whitespace

###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"
print #line of whitespace

n = 10
triangular = 0
myRange = range(0,n+1)             
# Create a range of numbers 0 - n and store myRange

for i in myRange:
    triangular = triangular + i    
    # For each number in myRange, add 1 through each iteration

print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

print #line of whitespace

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"
print #line of whitespace

n = 10
factorial = 1
for i in range(0,n):
    factorial = factorial * (i+1)  
    # For each number in range, add 1 through each iteration
    
print "%d!" %n + " =", factorial

print #line of whitespace

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"
print #line of whitespace

numlines = 10
for n in range(numlines,0,-1):
# runs through the range backwards from numlines to 0
    reverseFact = 1
    for i in range(0,n):
        reverseFact = reverseFact * (i+1)
        # For each number in range, add 1 through each iteration
    print reverseFact
        
print #line of whitespace

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"
print #line of whitespace

numlines = 10
for n in range(0,numlines):
    cumulative = 0
    fact = 1
    # declare variables for the second for loop
    for i in range(0,n):
        fact = fact * (i+1)
        cumulative = cumulative + (1.0/fact)
        # divides the whole factorial equation by 1.0 which gives the reciprocal
print "%.5f" % cumulative

###
### Collaboration
###

# Stackoverflow: "For loop with multiple condions in Python"
# http://stackoverflow.com/questions/8150846/for-loop-with-multiple-conditions-in-python

# Wiki Books: "Python Programming/Loops"
# http://en.wikibooks.org/wiki/Python_Programming/Loops

# Stackoverflow: "Python: How to make a list of n numbers and randomly select any number?"
# http://stackoverflow.com/questions/7567318/python-how-to-make-a-list-of-n-numbers-and-randomly-select-any-number

# My friend Dan helped me with Problem 1 to figure out on line 22 & 23 to iterate
# through a loop to add the numbers.

# My boyfriend helped me with Problem 5 to figure out that I only needed one 
# tab-over for my last 'print reverseFact' statement, instead of two-tab spaces.

# My boyfriend also helped me with Problem 6 to figure out that I needed to divide
# by'1.0' instead of just '1' on line 119. He also showed me how to use '%.5f".

###
### Reflection
###

# This assignment took me probably about 10 - 16 hours to complete including
# researching online. I didn't read Ch. 7 & 10 in 'Think Python' yet, but
# instead, I tried looking up loops, nested for loops, and how to print numbers
# backwards. The textbooks weren't much help, so I used the above websites and
# my friend Dan and boyfriend Eric. Problem 1, 4, and 5 were the most difficult
# for me. For Problem 4 & 5, I had 95% of the answer, but I was just missing
# one small thing wich my boyfriend helped me find. *See my collaboration above.
#
# The textbook readings and lecture didn't help me at all for this homework. 
# Lab2 helped me in learning how to clean-up my code a little bit. Overall, this
# homework was much more challenging than the first, but with a little bit of 
# help from the internet and my friends, I learned how to do it and enjoyed it.











