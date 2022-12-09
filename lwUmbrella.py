https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# Problem 2 - Part (b)

import sys
import numpy as np

# generate_samples(init_prob, evid_seq, T, E, n, size)
#   1. Randomly generate a number of sampels.
#
#   Parameters:
#     1. init_prob: Initial probabilities
#     2. evid_seq: Evidence seqeuence
#     3. T: T matrix
#     4. E: E matrix
#     5. n: Number of samples to be generated
#     6. size: Number of states in a sample
def generate_samples(init_prob, evid_seq, T, E, n, size):



# cal_weighted_prob_from_samples(samples)
#   1. Calculate the probability, based on the samples.
#
#   Parameters:
#     1. samples: Generated samples.
def cal_weighted_prob_from_samples(samples):



# cal_average_prob_and_var(probs)
#   1. Calculate the average probability, and its variance.
#
#   Parameters:
#     1. probs: A sequence of calculated probabilities.
def cal_average_prob_and_var(probs):



def main():
  n = int(sys.argv[1])
  size = int(sys.argv[2])
  evid_seq = []
  for i in range(size):
      evid_seq.append(int(sys.argv[i+3]))

  init_prob = [0.5, 0.5]
  T = np.matrix([[0.7, 0.3],[0.3, 0.7]])
  E = np.matrix([[0.9, 0.1],[0.2, 0.8]])

  probs = []
  for i in range(10):
    samples = generate_samples(init_prob, evid_seq, T, E, n, size)
    probs.append(cal_weighted_prob_from_samples(samples))
  
  prob_mean, var = cal_average_prob_and_var(probs)

  print("Estimated probability: ", prob_mean)
  print("Variance of the estimation: ", var)




if __name__ == "__main__":
  main()