# advent of code website: https://adventofcode.com/2021
# github: https://github.com/mullen25312/aoc2021

import os
import importlib

dailyPuzzles = ["d00", "d01", "d02"]

if __name__ == "__main__":

    for module in dailyPuzzles:
        # import daily module
        importedModule = importlib.import_module(module + ".dailyPuzzle")
        puzzle = importedModule.DailyPuzzle(os.path.join(module, "input.txt"))

        # solve puzzle
        puzzle.parse()
        puzzle.part_one()
        puzzle.part_two()

        # print results
        print(f"####### {module:s} - results #######")
        print(puzzle.part_one_result)
        print(puzzle.part_two_result)
