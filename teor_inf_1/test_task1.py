import unittest
from task1 import transition, NFA, DFA
from inputOutput import file_output, file_to_nfa_and_dfa

class TestNfaAndDfa(unittest.TestCase):
    def test1(self):
        nfa, dfa = file_to_nfa_and_dfa('example.txt')
        assert nfa.do("0") == True
        assert nfa.do("0 0") == False
        assert nfa.do("1") == False
        assert dfa == -1
    def test2(self):
        nfa, dfa = file_to_nfa_and_dfa('example1.txt')
        assert dfa != -1
        assert dfa.do("0") == False
        assert dfa.do("0 0") == True
    def test3(self):
        nfa, dfa = file_to_nfa_and_dfa('example2.txt')
        assert nfa.do("0") == True
        assert nfa.do("0 1 1") == True
        assert dfa == -1
