#!/bin/python3

import math
import os
import random
import re
import sys

def getWays(target_amount, available_coins):
    combinations_table = [0] * (target_amount + 1)
    combinations_table[0] = 1
    
    for coin in available_coins:
        for current_amount in range(coin, target_amount + 1):
            combinations_table[current_amount] += combinations_table[current_amount - coin]
            
    return combinations_table[target_amount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()