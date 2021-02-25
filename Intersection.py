class Intersection:
    streets = []
    schedule = []
    t = 0

    def __init__(self, id):
        self.id = id

    def addStreet(self, streetName, duration):
        self.schedule.extend([streetName] * duration)
        self.streets.append(streetName)

    def getActiveStreet(self):
        return self.schedule[self.t % len(self.schedule)]

    def __repr__(self):
        result = "%s: " % self.id
        for street in self.streets:
            result += "%s %s," % (street, self.schedule[self.t] == street)
        print(result)
        return result
