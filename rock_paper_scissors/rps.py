#!/usr/bin/python

import sys

# options = ['rock', 'paper', 'scissors']
# permutations = []

def rock_paper_scissors(n):
    options = ['rock', 'paper', 'scissors']
    permutations = []
    
    def find_results(rounds, results = []):
      if rounds == 0:
        return permutations.append(results)
      
      for i in range(len(options) - 1):
        new_result = results + [options[i]]
        find_results(rounds - 1, new_result)
    
    find_results(n, [])
    return permutations

print(rock_paper_scissors(1))

# def round_choice(rounds, round_number, n):
#     for i in range(len(options)):
#         print(options[i])
#         rounds.append(options[i])
#         if (round_number == n):
#             permutations.append(rounds)
#         else:
#             round_choice(rounds, round_number + 1, n)
#         rounds.pop()
#     return len(permutations)


# def rock_paper_scissors(n):
#     if n == 0:
#         return 0
#     else:
#         return round_choice([], 1, n)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
