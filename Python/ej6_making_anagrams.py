
"""
Given two strings,a  and ,b that may or may not be of the same length, determine 
the minimum number of character deletions required to  a  and b anagrams. Any characters
can be deleted from either of the strings.
"""
#
# Function 'makeAnagram'
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

from collections import Counter

def makeAnagram(a, b):
    # Write your code 
    c1 = Counter(a)
    for r in b:
        c1[r] -= 1
    val = c1.values()
    s = sum(abs(i) for i in val)
    
    return (s)