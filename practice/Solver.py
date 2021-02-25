class Solver:
    def __init__(self, input):
        self.input = input
        self.compilation_log = []

    def solve(self):
        target = self.input.targets[0]

        currentTime = 0
        currentTasks = [self.input.compiled_files[target["name"]]]

        serverStatus = []

        while(len(currentTasks) > 0):
            print("[%s] %s"%(currentTime, serverStatus))

            for server in serverStatus:

            currentTask = currentTasks.pop()

            self.compilation_log.append((currentTask.name, 1))

            for dependency in currentTask.dependencies:
                currentTasks.append(self.input.compiled_files[dependency])

            currentTime += 1

    def __str__(self):
        result = str(len(self.compilation_log)) + "\n"
        for compilation_step in self.compilation_log:
            result += compilation_step + "\n"
