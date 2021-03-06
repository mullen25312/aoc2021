from dxx.superDailyPuzzle import SuperDailyPuzzle

from itertools import combinations

# advent of code 2020 day 1 as template
class DailyPuzzle(SuperDailyPuzzle):
    def __init__(self, data_path):
        super().__init__(data_path)

    def parse(self, **kwargs):
        self.parsed = [int(line) for line in self.data.splitlines()]

    def part_one(self, **kwargs):
        pairs = list(combinations(self.parsed, 2))
        for pair in pairs:
            if sum(pair) == 2020:
                self.part_one_result = pair[0] * pair[1]

    def part_two(self, **kwargs):
        pairs = list(combinations(self.parsed, 3))
        for pair in pairs:
            if sum(pair) == 2020:
                self.part_two_result = pair[0] * pair[1] * pair[2]
