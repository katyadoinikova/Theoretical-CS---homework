import unittest
from task1 import transition, NFA, DFA
from inputOutput import file_output, file_to_nfa, file_to_dfa

class TestNfaAndDfa(unittest.TestCase):
    def test1(self):
        nfa = file_to_nfa('examples\example.txt')
        assert nfa.do("0") == True
        assert nfa.do("0 0") == False
        assert nfa.do("1") == False

    def test2(self):
        dfa = file_to_dfa('examples\example1.txt')
        assert dfa.do("0") == False
        assert dfa.do("0 0") == True
    def test3(self):
        nfa = file_to_nfa('examples\example2.txt')
        assert nfa.do("0") == True
        assert nfa.do("0 1 1") == True
