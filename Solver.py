from collections import defaultdict, Counter
from dataclasses import dataclass

from Intersection import Intersection


class Solver:
    def __init__(self, input):
        self.input = input
        self.intersections = self.getIntersectionList()

        self.getOutputFile()

    def solve(self):
        score = 0
        input = self.input
        intersections = self.getIntersectionList()


        for t in range(self.input.simTime):
            for intersection in intersections:
                # update lights
                intersection.step()

                # street with green light
                activeStreet = intersection.getActiveStreet()
                for street in self.input.streets.values():
                    street.step()

                    if (street == activeStreet):
                        if (len(street.segments[-1])):  # if there are cars waiting at light
                            movingCar = street.segments[-1].pop()  # just pick the first car for now
                            movingCar.route.pop(0)  # Car has already moved
                            if (len(movingCar.route) == 0):  # this car is done moving
                                score += self.input.scorePerCar
                            else:
                                self.input.streets[movingCar.route[0]].segments(0).append(street)
        print("SCORE: %d" % score)




        # for t in range(self.input.simTime):
        #     print("Time: %s" % t)
        #     # Turn on the lights
        #
        #     for street in self.input.streets.values():
        #         for i, segment in reversed(list(enumerate(street.segments))):
        #             segment.append(street.segments[i - 1])
        #             street.segments[i] = []
        #
        #         if (street.isLightGreen):
        #             if (len(street.segments[-1])):  # if there are cars waiting at light
        #                 movingCar = street.segments[-1].pop()  # just pick the first car for now
        #                 movingCar.route.pop()  # Car has already moved
        #                 if (len(movingCar.route) == 0):  # this car is done moving
        #                     score += self.input.scorePerCar
        #                 else:
        #                     self.input.streets[movingCar.route[0]].append(movingCar)

    def getIntersectionList(self):
        input = self.input
        intersectionMap = defaultdict(lambda: [])
        for _, street in input.streets.items():
            intersectionMap[street.endNode].append(street.name)

        intersections = []
        for id, intersectionMapping in intersectionMap.items():
            intersection = Intersection(id)
            for streetName in intersectionMapping:
                intersection.addStreet(streetName, 1) # set all the duration to 1

            intersections.append(intersection)

        return intersections

    def getOutputFile(self):
        result = "%s\n"%len(self.intersections)
        for intersection in self.intersections:
            result += "%s\n%s\n"%(intersection.id,len(intersection.streets))
            for pair in Counter(intersection.schedule).items():
                result += "%s %s\n"%(pair[0], pair[1])

        print(result)


