#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can astotale you have an infinite number of each denomination of
coin in the list
Your solution’s runtime will be evaluated in this task
"""
import sys
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Solution
    """
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[total] will have result
    if total <= 0:
        return 0
    m = len(coins)
    table = [0 for _ in range(total + 1)]

    # Base case (If given value total is 0)
    table[0] = 0

    # Initialize all table values as Infinite
    for i in range(1, total + 1):
        table[i] = sys.maxsize

    # Compute minimum coins required
    # for all values from 1 to total
    for i in range(1, total + 1):

        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1

    if table[total] == sys.maxsize:
        return -1

    return table[total]
