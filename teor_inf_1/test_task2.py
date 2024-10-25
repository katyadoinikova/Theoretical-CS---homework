import unittest
from task1 import transition, NFA, DFA
from task2 import DFA_from_NFA

from inputOutput import file_output, file_to_nfa_and_dfa


class TestNfaToDfa(unittest.TestCase):
    def test_1(self):
        nfa, dfa = file_to_nfa_and_dfa("example.txt")
        assert (dfa == -1)
        dfa_new = DFA_from_NFA(nfa)
        dfa_new.nfa_to_dfa(nfa)
        file_output("output_dfa_from_nfa1.txt", dfa_new)
        _, dfa_new_correct = file_to_nfa_and_dfa("output_dfa_from_nfa1.txt")
        nfa_ans, dfa_ans = file_to_nfa_and_dfa("test_ans1.txt")
        assert (dfa_ans != -1)
        assert (dfa_ans.alphabet == dfa_new_correct.alphabet)
        assert (dfa_ans.start_state[0] == dfa_new_correct.start_state[0])
        assert (dfa_ans.finish_states == dfa_new_correct.finish_states)
        assert (len(dfa_new_correct.transitions) == len(dfa_ans.transitions))
        for i in range(len(dfa_new_correct.transitions)):
            assert (dfa_new.transitions[i] == dfa_ans.transitions[i])
        assert (nfa.do("0") == dfa_new_correct.do("0"))
        assert (nfa.do("0 1 1") == dfa_new_correct.do("0 1 1"))

    def test_2(self):
        nfa, dfa = file_to_nfa_and_dfa("example2.txt")
        assert (dfa == -1)
        dfa_new = DFA_from_NFA(nfa)
        dfa_new.nfa_to_dfa(nfa)
        file_output("output_dfa_from_nfa2.txt", dfa_new)
        _, dfa_new_correct = file_to_nfa_and_dfa("output_dfa_from_nfa2.txt")
        nfa_ans, dfa_ans = file_to_nfa_and_dfa("test_ans2.txt")
        assert (dfa_ans != -1)
        assert (dfa_ans.alphabet == dfa_new_correct.alphabet)
        assert (dfa_ans.start_state[0] == dfa_new_correct.start_state[0])
        assert (dfa_ans.finish_states == dfa_new_correct.finish_states)
        assert (len(dfa_new_correct.transitions) == len(dfa_ans.transitions))
        for i in range(len(dfa_new_correct.transitions)):
            assert (dfa_new.transitions[i] == dfa_ans.transitions[i])
        assert (nfa.do("0") == dfa_new_correct.do("0"))
        assert (nfa.do("0 1 1") == dfa_new_correct.do("0 1 1"))
