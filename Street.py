from dataclasses import dataclass


@dataclass
class Street:
    startNode:int
    endNode: int
    name: str
    cost: int