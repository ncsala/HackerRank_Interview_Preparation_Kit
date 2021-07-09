# -*- coding: utf-8 -*-

#!/bin/python3

import os

#
# Complete the 'sockMerchant' function below.
#
# There is a large pile of socks that must be paired by color. Given an array of integers 
# representing the color of each sock, determine how many pairs of socks with matching colors there are.
# 
#  The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
# 
# Input Format
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers, , the colors of the socks in the pile.


def sockMerchant(n, ar):
    # Write your code here
    count = 0
    color = set()
    
    for r in range(len(ar)):
        if ar[r] not in color:
            color.add(ar[r])
        else:
            count += 1
            color.remove(ar[r])
        
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
