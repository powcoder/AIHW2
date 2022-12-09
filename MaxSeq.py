https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# Problem 1 - Part (b)

import sys
import numpy as np

# find_most_likely_seq(init_prob, evid_seq, T, E)
#   1. Find the most likely sequence of states.
#
#   Parameters:
#     1. init_prob: Initial probabilities
#     2. evid_seq: Evidence seqeuence
#     3. T: T matrix
#     4. E: E matrix
def find_most_likely_seq(init_prob, evid_seq, T, E):




# main()
#   1. Read users' input.
#   2. Find the most likely sequence of states.
def main():
  n = int(sys.argv[1])
  evid_seq = []
  for i in range(n):
      evid_seq.append(int(sys.argv[i+2]))

  T = np.matrix([[0.7, 0.3], [0.4, 0.6]])
  E = np.matrix([[0.9, 0.1], [0.3, 0.7]])
  init_prob = np.array([0.5, 0.5])
  max_seq = find_most_likely_seq(init_prob, evid_seq, T, E)
  n = len(max_seq)
  for i in range(n):
      print(max_seq[i], end=" ")
  print()




if __name__ == "__main__":
  main()