from collections import Counter, defaultdict

from Intersection import Intersection


class Solver:
    def __init__(self, input):
        self.input = input

    def solve(self):
        score = 0
        intersections = self.getIntersectionList(self.input.streets)

        # for t in range(self.input.simTime):
        #     print("Time: %s/%s" % (t, self.input.simTime))
        #     # print(self.input.streets)
        #     # Move all the cars forward
        #     for street in self.input.streets.keys():
        #         self.input.streets[street].step()
        #
        #     for intersection in intersections:
        #         # Move cars through intersection if the light is green
        #         activeStreet = self.input.streets[intersection.getActiveStreet()]
        #         if (len(activeStreet.segments[-1]) > 0):  # if there are cars waiting at light
        #             movingCar = self.input.streets[intersection.getActiveStreet()].segments[-1].pop(0)  # just pick the first car for now
        #             if (len(movingCar.route) == 0):  # this car is done moving
        #                 score += self.input.scorePerCar  # Add fixed score for car finishing path
        #                 score += self.input.simTime - t + 1  # Add point for each second left in the sim
        #             else:
        #                 nextStreet = movingCar.route.pop(0)  # Car has already moved
        #                 self.input.streets[nextStreet].segments[0].append(movingCar)
        #
        #         intersection.step()  # update lights

        print("SCORE: %d" % score)
        self.getOutputFile(intersections, score)

    def getIntersectionList(self, streets):
        intersectionMap = defaultdict(lambda: [])

        # print("Filtering unused streets")
        # print(len(self.input.streets))
        # self.input.streets = { key:value for (key,value) in self.input.streets.items() if streetLoads[key] > 0}
        # print(len(self.input.streets))

        for _, street in streets.items():
            intersectionMap[street.endNode].append(street.name)

        intersections = []
        for id, intersectionMapping in intersectionMap.items():
            intersection = Intersection(id)

            for streetName in intersectionMapping:
                intersection.addStreet(streetName, max(100 - len(self.input.streets[streetName].segments), 0))
                # intersection.addStreet(streetName, self.input.streets[streetName].load)

            intersection.setSchedule()
            intersections.append(intersection)

        return intersections

    def getOutputFile(self, intersections, score):
        result = "%s\n" % len(intersections)
        for intersection in intersections:
            counts = Counter(intersection.schedule)
            result += "%s\n%s\n" % (intersection.id, len(
                counts.keys()))  # Use counts.keys() because sometimes streets are not present in the schedule (the y are on for 0 seconds)
            for pair in counts.items():
                result += "%s %s\n" % (pair[0], pair[1])

        with open("results/%s_%s.txt" % (self.input.name, score), "w") as file:
            file.write(result)
