import os

from d00.dailyPuzzle import DailyPuzzle

if __name__ == "__main__":

    puzzle = DailyPuzzle(os.path.join("d00", "input.txt"))
    puzzle.parse_data()
    puzzle.solve_part_one()
    print(puzzle.part_one_result)
    puzzle.solve_part_two()
    print(puzzle.part_two_result)
