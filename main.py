#!/usr/bin/env python

import random
import string

from Stone import *

def random_chromosome(len = 20):
  return [ random.choice([0, 1, 2, 3]) for _ in range(len) ]

def connections(list, i, j):
  con = [0, 0, 0, 0]
  if i-1 >= 0: con[0] = list[i-1][j]
  if j+1 < 3: con[1] = list[i][j+1]
  if i+1 < 3: con[2] = list[i+1][j]
  if j-1 >= 0: con[3] = list[i][j-1]
  return con

def fitness():
  fits = 0
  for stone in Stone.list:
    fits = fits + stone.distance()
  return fits

# Initial state
inital_state = [
  [8, 7, 6],
  [5, 4, 3],
  [2, 1, 9]
]

# Place the stones
for i, l1 in enumerate(inital_state):
  for j, l2 in enumerate(l1):
    Stone(l2, ((3*i)+j), connections(inital_state, i, j))

if __name__ == "__main__":
  print random_chromosome()
  print fitness()