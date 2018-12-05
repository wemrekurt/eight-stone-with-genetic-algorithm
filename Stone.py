import math

class Stone:
  def __init__(self, value, position, connections):
    self.val = value
    self.pos = position

  def __mul__(self, other):
    other.pos, self.pos = self.pos, other.pos

  def __str__(self):
    return ("value: {}, position: {}, manhattan distance: {}"
    .format(self.val, self.pos, self.distance()))

  def distance(self):
    current = [float(self.pos/3), self.pos%3]
    value = self.val - 1
    target = [float(value/3), value%3]
    cur_dist = abs(current[0] - target[0])
    tar_dist = abs(current[1] - target[1])
    return int(round((cur_dist + tar_dist ) / 2))
