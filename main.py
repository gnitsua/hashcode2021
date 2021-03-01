import Input
from Solver import Solver
from Visualizer import Visualizer

if __name__ == "__main__":
    for file in "d":
        print("Running file: "+file)
        input = Input.parse(file)

        # visualizer = Visualizer()
        # visualizer.draw(input)

        solver = Solver(input)

        solution = solver.solve()