#!/usr/bin/python

import argparse
prices = [10, 7, 5, 8, 11, 9]
prices2 = [100, 90, 80, 50, 20, 10]

def find_max_profit(prices):
  # set max_profit to 0
  max_profit = 0
  # loop through the array of prices with index i
  # pick price at index i
  for i in range(0, len(prices) - 1):
  # loop through the array of prices with index j from index i + 1
    for j in range(i + 1, len(prices)):
  # if price at j minus price at i is greater than max_profit, set max_profit
      current_profit = prices[j] - prices[i]
      if current_profit > max_profit:
        max_profit = current_profit
  # return max_profit
  return max_profit
    
  # pass
print(find_max_profit(prices2))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))