#!/bin/python3

import math
import os
import random
import re
import sys
def hour(a,row,col):
    b=[]
    for i in range(row,row+3):
        for j in range(col,col+3):
            b.append(a[i][j])
    return sum(b)-b[3]-b[5]
# Complete the hourglassSum function below.
def hourglassSum(arr):
    c=[]           
    for i in range(4):
        for j in range(4):
            c.append(hour(arr,i,j))
    return max(c)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
