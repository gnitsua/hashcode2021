from Input import Input
from Solver import Solver

if __name__ == "__main__":
    for file in "abcdef":
        input = Input.parse(file)

        solver = Solver(input)

        solution = solver.solve()