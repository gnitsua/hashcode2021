from dataclasses import dataclass
from typing import List


@dataclass
class Street:
    def __init__(self, startNode, endNode, name, cost):
        self.startNode = startNode
        self.endNode = endNode
        self.name = name
        self.load = 0
        self.segments = [[] for i in range((cost + 1))]  # Streets with a cost of 1 actually need 2 segments (so a car takes one tick to move from start to the light)


    # | 1 | | | 2 |
    # | | 1 | | 2 |
    def step(self):
        for i in reversed(range(1, len(self.segments))):
            self.segments[i].extend(self.segments[i-1])
            self.segments[i-1] = []

    def __repr__(self):
        return str(self.segments)
