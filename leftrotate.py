#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def leftrotatebyone(a):
    return a[1:len(a)]+a[0:1]
def rotLeft(a, d):
    d=d%len(a)
    a=a[d:]+a[:d]
    return a
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
