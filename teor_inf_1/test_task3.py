import unittest
from task3 import minimize


class TestFind01101(unittest.TestCase):
    def test_find_01101_1(self):
        automaton = Automaton("automata/find_01101.txt")
        result = automaton.is_accept("000101011010")
        self.assertEqual(result, True)