# import yaml
import pytest
import importlib
import os

# import unittest

# from dxx.superDailyPuzzle import SuperDailyPuzzle


# class TestConfig:
#     parse_args: None
#     part_one_args: None
#     part_two_args: None

#     parse_res: None
#     part_one_res: None
#     part_two_res: None

#     # def __init__(self, config):
#     #     if config == None:
#     #         config = {}

#     #     self.parse_args = config.get("parse_args") or {}
#     #     self.part_one_args = config.get("part_one_args") or {}
#     #     self.part_two_args = config.get("part_two_args") or {}

#     #     self.parse_res = config.get("parse_res") or ""
#     #     self.part_one_res = config.get("part_one_res") or ""
#     #     self.part_two_res = config.get("part_two_res") or ""


# class Testing(unittest.TestCase):
class Tests_d00:
    importedModule = importlib.import_module("d00" + ".dailyPuzzle")
    puzzle = importedModule.DailyPuzzle(os.path.join("d00", "input.txt"))
    # test_config: TestConfig
    # puzzle: SuperDailyPuzzle

    # def __init__(self, puzzle, config_path):
    #     self.puzzle = puzzle
    #     with open(config_path, "r") as file:
    #         self.test_config = TestConfig(yaml.load(file, Loader=yaml.FullLoader))

    # def setup(self):
    #     pass

    # def teardown(self):
    #     pass

    def test_part_one(self):
        self.puzzle.parse()
        self.puzzle.part_one()

        # assert True  # self.puzzle.parsed == self.test_config.parse_res
        assert self.puzzle.part_one_result == 542619

    def test_part_two(self):
        self.puzzle.parse()
        self.puzzle.part_two()
        # assert True  # self.puzzle.parsed == self.test_config.parse_res
        assert self.puzzle.part_two_result == 32858450


class Tests_d01:
    importedModule = importlib.import_module("d01" + ".dailyPuzzle")
    puzzle = importedModule.DailyPuzzle(os.path.join("d01", "input.txt"))

    def test_part_one(self):
        self.puzzle.parse()
        self.puzzle.part_one()
        assert self.puzzle.part_one_result == 1692

    def test_part_two(self):
        self.puzzle.parse()
        self.puzzle.part_two()
        assert self.puzzle.part_two_result == 1724


class Tests_d02:
    importedModule = importlib.import_module("d02" + ".dailyPuzzle")
    puzzle = importedModule.DailyPuzzle(os.path.join("d02", "input.txt"))

    def test_part_one(self):
        self.puzzle.parse()
        self.puzzle.part_one()
        assert self.puzzle.part_one_result == 2120749

    def test_part_two(self):
        self.puzzle.parse()
        self.puzzle.part_two()
        assert self.puzzle.part_two_result == 2138382217
