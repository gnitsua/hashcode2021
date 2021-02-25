from Input import Input
from Solver import Solver

if __name__ == "__main__":
    input = Input.parse("a")

    solver = Solver(input)

    solution = solver.solve()