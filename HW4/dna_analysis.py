# Name: Jessica Morton
# Evergreen Login: morjes14
# Computer Science Foundations
# Programming as a Way of Life
# Homework 4: DNA analysis (Part 2)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far
total_count = 0
# Number of G and C nucleotides seen so far
gc_count = 0
# Number of A and T nucleotides seen so far
at_count = 0
# Number of g, c, a, and t nucleotides seen so far
g_count = 0
c_count = 0
a_count = 0
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

    # next, if the bp is a A or a T,
    if bp == 'T' or bp == 'A':
        # increment the count of at
        at_count = at_count + 1

    # next, if the bp is a G        
    if bp == 'G':
        # increment the count of g
        g_count = g_count + 1
    
    # next, if the bp is a C                  
    if bp == 'C':
        # increment the count of c
        c_count = c_count + 1     
    
    # next, if the bp is an A   
    if bp == 'A':
        # increment the count of a
        a_count = a_count + 1   
    
    # next, if the bp is a T  
    if bp == 'T':
        # increment the count of t
        t_count = t_count + 1   
        
# Total of A, T, C, G
gcat_total = gc_count + at_count
# sum of all G, C, A, and T
sum_count = g_count + c_count + a_count + t_count
# divide the gc_count and ac_count by the total_count
gc_content = float(gc_count) / gcat_total
at_content = float(at_count) / gcat_total
# divide the at_content by the gc_content
atgc_ratio = float(at_content / gc_content)

# find GC Classification
if gc_content > float(0.60):
    
    gc_classif = 'high GC content'
    
elif gc_content < float(0.40):
    
    gc_classif = 'low GC content'
    
else:
    
    gc_classif = 'moderate GC content'


# Print the answers
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G count:', g_count
print 'C count:', c_count
print 'A count:', a_count
print 'T count:', t_count
print 'Sum count:', sum_count
print 'Total count:', total_count
print 'Seq length:', len(seq)
print 'AT/GC Ratio:', atgc_ratio
print 'GC Classification:', gc_classif