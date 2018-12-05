#!/usr/bin/env python

import random
import string
import copy

from Stone import *

# create random chromosomes
def random_chromosome(len = 20):
  return [ random.choice([0, 1, 2, 3]) for _ in range(len) ]

# create connections
def connections(list, i, j):
  con = [0, 0, 0, 0]
  if i-1 >= 0: con[0] = list[i-1][j]
  if j+1 < 3: con[1] = list[i][j+1]
  if i+1 < 3: con[2] = list[i+1] [j]
  if j-1 >= 0: con[3] = list[i][j-1]
  return con

# calculates stones manhattan distances
def calculate_distance(stones):
  fits = 0
  for stone in stones:
    fits = fits + stone.distance()
  return fits

def get_position(stones):
  for i in stones:
    if i.val == 9: return i.pos
  return 8

def valid_moves(pos, i = None):
  mov = []
  if pos > 2: mov.append(0)
  if (pos % 3) < 2: mov.append(1)
  if pos < 6: mov.append(2)
  if (pos % 3) > 0: mov.append(3)
  if (not(i is None)) and (i in mov) : mov.remove(i)
  return mov

# movements
def move(stones, chromosome):
  print(chromosome)
  return 3

def mutation(valid):
  return random.choice(valid)

def fitness(position, chromosome):
  for i in range(0, len(chromosome)-3):
    if (chromosome[i] == chromosome[i+2]) and (chromosome[i+1] == chromosome[i+3]):
      chromosome[i] = mutation(valid_moves(position, chromosome[i]))
    elif chromosome[i] == chromosome[i+1] and chromosome[i] == chromosome[i+2]:
      chromosome[i+2] = mutation(valid_moves(position, chromosome[i]))
  return chromosome

def check_fitness(position, population):
  for i, chromosome in enumerate(population):
    population[i] = fitness(position, chromosome)  
  return population

# Initial state
inital_state = [
  [8, 7, 6],
  [5, 4, 3],
  [2, 9, 1]
]

stones = []
# Place the stones
for i, l1 in enumerate(inital_state):
  for j, l2 in enumerate(l1):
    stones.append(Stone(l2, ((3*i)+j), connections(inital_state, i, j)))

if __name__ == "__main__":
  population = [ random_chromosome() for _ in range(100) ]
  position = get_position(stones)
  for i in check_fitness(position, population):
    print(i)