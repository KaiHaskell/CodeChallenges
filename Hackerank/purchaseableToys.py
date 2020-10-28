import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):
    # first sort the toys so the cheapest will be purchased first
    prices.sort()
    counter = 0
    i = 0
    # iterate over the prices and subtract the toy prices until we run out of money
    for price in prices:
        if k >= price:
            k -= price
            # increment our counter for each toy purchased
            counter += 1
        else:
            # once we can no longer purchase toys we are finished
            return counter
    # return the counter
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
