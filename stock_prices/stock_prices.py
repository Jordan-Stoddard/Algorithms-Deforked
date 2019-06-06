#!/usr/bin/python

import argparse

"""
I'll need to loop through the array
Stock prices come in one at a time, from left to right.
Loop through the array from right to left,
For each item, loop through from right to left again, checking the differential of the first loops
current index against the second loops current index. If the current index's differential is less than
the previous lowest differential set, set the current index's differential to be the lowest.
Once loop(s) are complete, return lowest differential 
"""

def find_max_profit(prices):
    profit = prices[len(prices)-1] - prices[len(prices)-2]
    for i in range(len(prices)-1, -1, -1):
        for j in range(i-1, -1, -1):
            current_profit = prices[i] - prices[j]
            if current_profit > profit:
              profit = current_profit

    return profit

# print(find_max_profit([100, 90, 80, 50, 20, 10]))
print(find_max_profit([1050, 270, 1540, 3800, 2]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))