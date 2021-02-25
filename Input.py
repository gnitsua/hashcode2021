from dataclasses import dataclass
from typing import List

from Route import Route
from Street import Street


@dataclass
class Input:
    name: str
    simTime: int
    streets: dict
    routes: List
    scorePerCar: int

    @staticmethod
    def parse(filename):
        lineCount = len(open("input/" + filename + ".txt", "r").readlines())
        with open("input/" + filename + ".txt", "r") as file:
            inputInfoLine = file.readline().strip("\n").split(" ")
            assert (len(inputInfoLine) == 5)

            simTime, numIntersections, numStreets, numCars, scorePerCar = inputInfoLine

            intersections = {}
            for _ in range(0, lineCount - int(numCars) - 1):  # read in the intersections
                intersectionInfoLine = file.readline().strip("\n").split(" ")
                assert (len(intersectionInfoLine) == 4)

                intersections[intersectionInfoLine[2]] = Street(int(intersectionInfoLine[0]),
                                            int(intersectionInfoLine[1]),
                                            intersectionInfoLine[2],
                                            int(intersectionInfoLine[3]))

            routes = []
            for _ in range(0, int(numCars) - 1):
                routeInfoLine = file.readline().strip("\n").split(" ")
                numSteps = int(routeInfoLine[0])
                assert (numSteps == len(routeInfoLine) - 1)
                routes.append(Route(routeInfoLine[1:]))

            return Input(filename, int(simTime), intersections, routes, int(scorePerCar))
