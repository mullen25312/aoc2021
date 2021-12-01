import os
import importlib

dailyPuzzles = ["d00"]

if __name__ == "__main__":

    for module in dailyPuzzles:

        importedModule = importlib.import_module(module + ".dailyPuzzle")
        puzzle = importedModule.DailyPuzzle(os.path.join(module, "input.txt"))
        puzzle.parse()
        puzzle.part_one()
        print(puzzle.part_one_result)
        puzzle.part_two()
        print(puzzle.part_two_result)

