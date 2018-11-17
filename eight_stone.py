#!/usr/bin/env python

import random
import string

def random_chromosome(len = 20):
  return [ random.choice(['t', 'r', 'b', 'l']) for _ in range(len) ]

if __name__ == "__main__":
  print random_chromosome()
