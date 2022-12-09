https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# Problem 1 - Part (a)

import sys
import numpy as np

# forward(pri_prob, evid_seq, T, E)
#   1. Calculate the sequence of forward probabilities.
#
#   Parameters:
#     1. init_prob: Initial probabilities
#     2. evid_seq: Evidence seqeuence
#     3. T: T matrix
#     4. E: E matrix
def forward(init_prob, evid_seq, T, E):



# backward(last_prob, evid_seq, T, E)
#   1. Calculate the sequence of backward probabilities.
#
#   Parameters:
#     1. last_prob: Last probabilities
#     2. evid_seq: Evidence seqeuence
#     3. T: T matrix
#     4. E: E matrix
def backward(last_prob, evid_seq, T, E):



# smooth(init_prob, last_prob, evid_seq, T, E)
#   1. Calculate the smoothed estimates, given the sequence of evidence.
#
#   Parameters:
#     1. init_prob: Initial probabilities
#     2. last_prob: Last probabilities
#     3. evid_seq: Evidence seqeuence
#     4. T: T matrix
#     5. E: E matrix
def smooth(init_prob, last_prob, evid_seq, T, E):




# main()
#   1. Read users' input.
#   2. Calculate the smoothed estimates.
def main():
  n = int(sys.argv[1])
  evid_seq = []
  for i in range(n):
      evid_seq.append(int(sys.argv[i+2]))

  T = np.matrix([[0.7, 0.3], [0.4, 0.6]])
  E = np.matrix([[0.9, 0.1], [0.3, 0.7]])
  init_prob = np.array([0.5, 0.5])
  last_prob = np.array([1, 1])
  ans = smooth(init_prob, last_prob, evid_seq, T, E)
  n = len(ans)
  for i in range(n):
      print(ans[i][0], end=" | ")
  print()




if __name__ == "__main__":
  main()