import math


class Intersection:
    def __init__(self, id):
        self.id = id
        self.streets = []
        self.streetWeights = []
        self.schedule = []
        self.t = 0

    def addStreet(self, streetName, weight):
        self.streets.append(streetName)
        self.streetWeights.append(weight)

    def setSchedule(self):
        assert len(self.streets) == len(self.streetWeights)

        cycleLengths = self.getCycleLengths()
        # sortedByCycleLength = sorted(zip(self.streets, cycleLengths), key=lambda pair: pair[1], reverse=True) # Didn't help
        for streetName, cycleLength in zip(self.streets, cycleLengths):
            self.schedule.extend([streetName] * cycleLength)

    def getCycleLengths(self):
        totalWeight = sum(self.streetWeights)

        # if (totalWeight == 0):  # if the total weight is 0, just default to 1 second per street
        if (totalWeight == 0):  # if the total weight is 0, just default to 1 second per street
            cycleLengths = [1] * len(self.streetWeights)
        else:
            cycleLengths = list(
                map(lambda streetWeight:
                    math.ceil(math.log(streetWeight+0.01, 2.86)),  # worked well on C
                    # math.ceil((streetWeight / totalWeight) * (1 * len(self.streets))),  # did will on E
                    # math.ceil((streetWeight / totalWeight) * (2 * len(self.streets))), # did will on F
                    self.streetWeights))

        return cycleLengths

    def getActiveStreet(self):
        return self.schedule[self.t % len(self.schedule)]

    def step(self):
        self.t += 1

    def __repr__(self):
        result = "%s: " % self.id
        for street in self.streets:
            result += "%s %s," % (street, self.schedule[self.t] == street)
        print(result)
        return result
