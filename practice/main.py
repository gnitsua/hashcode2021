from Input import Input
from practice.Solver import Solver

if __name__ == "__main__":
    input = Input.parse("a_example.in")

    print(input)

    solution = Solver(input).solve()