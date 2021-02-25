class Solver:
    def __init__(self, input):
        self.input = input
        self.compilation_log = []

    def solve(self):
        target = self.input.targets[0]

        currentTime = 0
        currentTask = self.input.compiled_files[target["name"]]
        while(currentTime < target["deadline"]):
            self.compilation_log.append((currentTask.name, 1))
            currentTime += currentTask.compile_time
            
        pass

    def __str__(self):
        result = str(len(self.compilation_log)) + "\n"
        for compilation_step in self.compilation_log:
            result += compilation_step + "\n"
