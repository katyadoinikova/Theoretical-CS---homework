import unittest
from task1 import transition
from inputOutput import file_output_norm, file_to_dfa
from task3 import minimize, equivalent, accepts_all


class TestMinimize(unittest.TestCase):
    def test1(self):
        dfa = file_to_dfa("examples\example1.txt")
        min_dfa = minimize(dfa)
        file_output_norm("min_out_1.txt", min_dfa)
        self.assertEqual(min_dfa.states_size, 2)
        self.assertEqual(min_dfa.start_state, 0)
        self.assertEqual(min_dfa.finish_states, {0})
        self.assertEqual(min_dfa.transitions[0], transition(0, 0, 1))
        self.assertEqual(min_dfa.transitions[1], transition(1, 0, 0))

    def test2(self):
        dfa = file_to_dfa("examples\example3.txt")
        min_dfa = minimize(dfa)
        file_output_norm("min_out_2.txt", min_dfa)
        self.assertEqual(min_dfa.states_size, 4)
        self.assertEqual(len(min_dfa.finish_states), 2)
        dfa_ans = file_to_dfa("test_ans_for_minimize1.txt")
        self.assertEqual(dfa_ans.alphabet, min_dfa.alphabet)
        self.assertEqual(dfa_ans.start_state, min_dfa.start_state)
        self.assertEqual(dfa_ans.finish_states, min_dfa.finish_states)
        self.assertEqual(len(min_dfa.transitions), len(dfa_ans.transitions))
        for i in range(len(min_dfa.transitions)):
            self.assertEqual(min_dfa.transitions[i], dfa_ans.transitions[i])

    def test3(self):
        dfa = file_to_dfa("examples\example4.txt")
        min_dfa = minimize(dfa)
        file_output_norm("min_out_3", min_dfa)
        dfa_ans = file_to_dfa("test_ans_for_minimize2.txt")
        self.assertEqual(equivalent(min_dfa, dfa_ans), True)
    def test4(self):
        dfa = file_to_dfa("examples\example5.txt")
        min_dfa = minimize(dfa)
        file_output_norm("min_out_4", min_dfa)
        self.assertEqual(min_dfa.states_size, 1)
        self.assertEqual(min_dfa.start_state, 0)
        self.assertEqual(min_dfa.finish_states, {0})
        self.assertEqual(min_dfa.transitions[0], transition(0, 0, 0))
        self.assertEqual(min_dfa.transitions[1], transition(0, 1, 0))


class TestEq(unittest.TestCase):
    def test1(self):
        dfa = file_to_dfa("examples\example1.txt")
        min_dfa = minimize(dfa)
        self.assertEqual(equivalent(min_dfa, dfa), True)

    def test2(self):
        dfa = file_to_dfa("examples\example3.txt")
        min_dfa = minimize(dfa)
        self.assertEqual(equivalent(min_dfa, dfa), True)

    def test3(self):
        dfa = file_to_dfa("examples\example4.txt")
        min_dfa = minimize(dfa)
        self.assertEqual(equivalent(min_dfa, dfa), True)

    def test4(self):
        dfa1 = file_to_dfa("examples\example3.txt")
        dfa2 = file_to_dfa('examples\example4.txt')
        self.assertEqual(equivalent(dfa1, dfa2), False)

    def test5(self):
        dfa1 = file_to_dfa("examples\example3.txt")
        dfa2 = file_to_dfa('examples\example_for_eq.txt')
        self.assertEqual(equivalent(dfa1, dfa2), True)

class TestAcceptsAll(unittest.TestCase):
    def test1(self):
        dfa = file_to_dfa("examples\example3.txt")
        self.assertEqual(accepts_all(dfa), False)

    def test2(self):
        dfa = file_to_dfa("examples\example_accept_all.txt")
        self.assertEqual(accepts_all(dfa), True)

    def test3(self):
        dfa = file_to_dfa("examples\example_accept_just_empty.txt")
        self.assertEqual(accepts_all(dfa), False)


