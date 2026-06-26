#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    char_counts = Counter(s)
    freq_counts = Counter(char_counts.values())
    
    if len(freq_counts) == 1:
        return "YES"
    
    if len(freq_counts) > 2:
        return "NO"
    
    (f1, c1), (f2, c2) = freq_counts.items()
    
    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        return "YES"
        
    if (f1 - f2 == 1 and c1 == 1) or (f2 - f1 == 1 and c2 == 1):
        return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()