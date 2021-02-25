from dataclasses import dataclass
from typing import List

from Street import Street
from Route import Route


@dataclass
class Input:
    simTime: int
    intersections: List
    routes: List

    @staticmethod
    def parse(filename):
        lineCount =
        with open("input/" + filename, "r") as file:
            inputInfoLine = file.readline().strip("\n").split(" ")
            assert (len(inputInfoLine) == 5)

            simTime, numIntersections, numStreets, numCars, score = inputInfoLine

            intersections = []
            for _ in range(0, int(numIntersections)): # read in the intersections
                intersectionInfoLine = file.readline().strip("\n").split(" ")
                assert (len(intersectionInfoLine) == 4)

                intersections.append(Street(int(intersectionInfoLine[0]),
                                            int(intersectionInfoLine[1]),
                                            intersectionInfoLine[2],
                                            int(intersectionInfoLine[3])))

            routes = []
            for route in reversed(open("input/" + filename, "r").readlines()): # Open the file a second time
                routeInfoLine = route
                numSteps = int(routeInfoLine[0])
                assert(numSteps == len(routeInfoLine) + 1)
                routes.append(Route(routeInfoLine[1:]))


            return Input(simTime, intersections, routes)

