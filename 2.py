#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
        r = s[::-1]
        for i in range(1, len(s)):
            a = abs(ord(s[i]) - ord(s[i - 1]))
            b = abs(ord(r[i]) - ord(r[i - 1]))
            if a != b:
                return "Not Funny"
                
        else:
            return "Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
