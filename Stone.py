import math

class Stone:
  list = []
  def __init__(self, value, position, connections):
    self.val = value
    self.pos = position
    self.connections = connections
    Stone.list.append(self)

  def __mul__(self, other):
    if other.val in self.connections:
      other.connections, self.connections = self.connections, other.connections
      other.pos, self.pos = self.pos, other.pos
      si = self.connections.index(self.val)
      oi = other.connections.index(other.val)
      self.connections[si] = other.val
      other.connections[oi] = self.val

  def __str__(self):
    return ("value: {}, position: {}, connections: {}, manhattan distance: {}"
    .format(self.val, self.pos, self.connections, self.distance()))

  def distance(self):
    current = [float(self.pos/3), self.pos%3]
    value = self.val - 1
    target = [float(value/3), value%3]
    cur_dist = abs(current[0] - target[0])
    tar_dist = abs(current[1] - target[1])
    return int(round((cur_dist + tar_dist ) / 2))
