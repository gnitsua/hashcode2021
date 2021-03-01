from collections import defaultdict
from dataclasses import dataclass
from typing import List

from Car import Car
from Intersection import Intersection
from Street import Street
import numpy as np


@dataclass
class Input:
    name: str
    simTime: int
    streets: dict
    cars: List
    scorePerCar: int


def parse(filename):
    lineCount = len(open("input/" + filename + ".txt", "r").readlines())
    with open("input/" + filename + ".txt", "r") as file:
        inputInfoLine = file.readline().strip("\n").split(" ")
        assert (len(inputInfoLine) == 5)

        simTime, numIntersections, numStreets, numCars, scorePerCar = inputInfoLine

        streets = {}
        for _ in range(0, lineCount - int(numCars) - 1):  # read in the intersections
            intersectionInfoLine = file.readline().strip("\n").split(" ")
            assert (len(intersectionInfoLine) == 4)

            streets[intersectionInfoLine[2]] = Street(int(intersectionInfoLine[0]),
                                                      int(intersectionInfoLine[1]),
                                                      intersectionInfoLine[2],
                                                      int(intersectionInfoLine[3]))

        cars = []
        routeLengths = []
        for _ in range(0, int(numCars)):
            routeInfoLine = file.readline().strip("\n").split(" ")
            numSteps = int(routeInfoLine[0])
            assert (numSteps == len(routeInfoLine) - 1)

            car = Car(routeInfoLine[1:])
            cars.append(car)

            for i, streetName in enumerate(car.route):
                streets[streetName].load += 1 # Start with just fixed weight
                routeLengths.append(len(car.route))
                # streets[streetName].load += len(car.route) # weight nodes that are on long routes

            startingStreet = car.route.pop(0) # Remove the street from the route since we're already there
            streets[startingStreet].segments[-1].append(car)
            # print(streets)

        print(np.histogram(routeLengths))

        return Input(filename, int(simTime), streets, cars, int(scorePerCar))




