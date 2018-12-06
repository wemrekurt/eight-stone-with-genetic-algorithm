#!/usr/bin/env python

import random
import string
import copy
import operator
from operator import itemgetter

from Stone import Stone

# create random chromosomes
def random_chromosome(len = 20):
  return [ random.choice([0, 1, 2, 3]) for _ in range(len) ]

def print_board(stones):
  for stone in sorted(stones.values(), key=operator.attrgetter('pos')):
    if (stone.pos+1) % 3 == 0:
      print("%d" % stone.val)
    else:
      print("%d" % stone.val),

def chunk_it(a_list):
  half = len(a_list)//2
  return [a_list[:half], a_list[half:]]

def find_with_position(stones, pos):
  for i in stones:
    if(stones[i].pos == pos): 
      return stones[i].val
  return 9

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
  for i in stones:
    fits = fits + stones[i].distance()
  return fits

def valid_moves(pos, i = None):
  mov = []
  if pos > 2: mov.append(0)
  if (pos % 3) < 2: mov.append(1)
  if pos < 6: mov.append(2)
  if (pos % 3) > 0: mov.append(3)
  if (not(i is None)) and (i in mov) : mov.remove(i)
  return mov

def target_position(position, movement):
  if movement == 0 and position > 2: return position - 3
  if movement == 1 and (position % 3) < 2: return position + 1
  if movement == 2 and position < 6: return position + 3
  if movement == 3 and (position % 3) > 0: return position - 1
  return None

# movements
def move(stones, chromosome):
  stones = copy.deepcopy(stones)
  stone = stones[9]
  for i in chromosome:
    pos = target_position(stone.pos, i)
    if not(pos is None):
      if calculate_distance(stones) == 0:
        print_board(stones)
        return(0)
      stone * stones[find_with_position(stones, pos)]
  return calculate_distance(stones)

def mutation(valid):
  return random.choice(valid)

def fitness(position, chromosome):
  for i in range(0, len(chromosome)-3):
    if (chromosome[i] == chromosome[i+2]) and (chromosome[i+1] == chromosome[i+3]):
      chromosome[i] = mutation(valid_moves(position, chromosome[i]))
    elif chromosome[i] == chromosome[i+1] and chromosome[i] == chromosome[i+2]:
      chromosome[i+2] = mutation(valid_moves(position, chromosome[i+2]))
  return chromosome

def check_fitness(position, population):
  for i, chromosome in enumerate(population):
    population[i] = fitness(position, chromosome)  
  return population

def crossover(c1, c2):
  x1 = chunk_it(c1)
  x2 = chunk_it(c2)
  return [x1[0] + x2[1], x2[0] + x1[1]]

def create_generation(chros):
  population = []
  chros = sorted(chros, key=itemgetter('fitness'))
  length = len(chros)/2
  for i in range(0, length):
    population = population + (crossover(chros[i]['chromosome'], chros[i+length]['chromosome']))
  return population

def work(population, stones, generation):
  position = stones[9].pos
  fitness_values = []
  for i in check_fitness(position, population):
    fitness = move(stones, i)
    if fitness == 0:
      print("Solution: {} Generation: {}, ".format(i, generation))
      return None
    else:
      fitness_values.append({ 'fitness': fitness, 'chromosome': i})
  if generation < 300:
    new_population = create_generation(fitness_values)
    print("Generation: {}, Population: {}, Fitness: ".format(generation, len(new_population)))
    work(new_population, stones, generation + 1)


# Initial state
inital_state = [
  [1, 2, 3],
  [7, 9, 5],
  [4, 8, 6]
]

stones = {}
# Place the stones
for i, l1 in enumerate(inital_state):
  for j, l2 in enumerate(l1):
    stones[l2] = (Stone(l2, ((3*i)+j), connections(inital_state, i, j)))

if __name__ == "__main__":
  print('initial state:')
  print_board(stones)
  print('----------')
  population = [ random_chromosome() for _ in range(100) ]
  work(population, stones, 1)