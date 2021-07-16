



#!/bin/python3

"""There is a string, s , of lowercase English letters that is repeated infinitely many times.
Given an integer, n , find and print the number of letter a's in the first n letters of the 
infinite string. """


import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code
    conta = 0
    
    #contar el numero de a's en s
    for r in range(len(s)):
        if s[r] == 'a':
            conta += 1
        
    # contar el numero de a's en las full instances de s
    m = math.floor(n / len(s))
    conta *= m
    
    #contar las a's faltantes
    str2 = s[0:n-m*len(s)]
    for i in range(len(str2)):
     if str2[i] == 'a':
         conta += 1
    
    return (conta)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
