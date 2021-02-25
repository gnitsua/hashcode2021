from dataclasses import dataclass
from typing import List


@dataclass
class Street:
    def __init__(self, startNode, endNode, name, cost):
        self.startNode = startNode
        self.endNode = endNode
        self.name = name
        self.isLightGreen = False
        self.segments = [[]] * cost

    def step(self):
        for i, segment in reversed(list(enumerate(self.segments))):
            segment.append(self.segments[i - 1])
            self.segments[i] = []
