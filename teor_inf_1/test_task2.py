import unittest
from task1 import transition, NFA, DFA
from task2 import DFA_from_NFA

from inputOutput import file_output, file_to_nfa, file_to_dfa


class TestNfaToDfa(unittest.TestCase):
    def test_1(self):
        nfa = file_to_nfa("examples\example.txt")

        dfa_new = DFA_from_NFA(nfa)
        dfa_new.nfa_to_dfa(nfa)
        file_output("output_dfa_from_nfa1.txt", dfa_new)
        dfa_new_correct = file_to_dfa("output_dfa_from_nfa1.txt")
        dfa_ans = file_to_dfa("test_ans1.txt")
        self.assertEqual(dfa_ans.alphabet, dfa_new_correct.alphabet)
        self.assertEqual(dfa_ans.start_state, dfa_new_correct.start_state)
        self.assertEqual(dfa_ans.finish_states, dfa_new_correct.finish_states)
        self.assertEqual(len(dfa_new_correct.transitions), len(dfa_ans.transitions))
        for i in range(len(dfa_new_correct.transitions)):
            self.assertEqual(dfa_new.transitions[i], dfa_ans.transitions[i])
        self.assertEqual(nfa.do("0"), dfa_new_correct.do("0"))
        self.assertEqual(nfa.do("0 1 1"), dfa_new_correct.do("0 1 1"))

    def test_2(self):
        nfa = file_to_nfa("examples\example2.txt")
        dfa_new = DFA_from_NFA(nfa)
        dfa_new.nfa_to_dfa(nfa)
        file_output("output_dfa_from_nfa2.txt", dfa_new)
        dfa_new_correct = file_to_dfa("output_dfa_from_nfa2.txt")
        dfa_ans = file_to_dfa("test_ans2.txt")
        self.assertEqual(dfa_ans.alphabet, dfa_new_correct.alphabet)
        self.assertEqual(dfa_ans.start_state, dfa_new_correct.start_state)
        self.assertEqual(dfa_ans.finish_states, dfa_new_correct.finish_states)
        self.assertEqual(len(dfa_new_correct.transitions), len(dfa_ans.transitions))
        for i in range(len(dfa_new_correct.transitions)):
            self.assertEqual(dfa_new.transitions[i], dfa_ans.transitions[i])
        self.assertEqual(nfa.do("0"), dfa_new_correct.do("0"))
        self.assertEqual(nfa.do("0 1 1"), dfa_new_correct.do("0 1 1"))
