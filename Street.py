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