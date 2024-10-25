import filecmp

from task1 import transition, NFA, DFA
from task2 import DFA_from_NFA
from task4 import RegexVM, Instruction, compile_regex
from inputOutput import file_output, file_to_nfa_and_dfa





def test_1():
    nfa, dfa = file_to_nfa_and_dfa("example2.txt")
    assert(dfa == -1)
    dfa_new = DFA_from_NFA(nfa)
    dfa_new.nfa_to_dfa(nfa)
    file_output("output.txt", dfa_new)
    nfa_ans, dfa_ans = file_to_nfa_and_dfa("test_ans1.txt")
    assert(dfa_ans != -1)
    assert(dfa_ans.alphabet == dfa_new.alphabet)
    assert (dfa_ans.start_state[0] == dfa_new.start_state)
    assert (dfa_ans.finish_states == dfa_new.finish_states)

test_1()

pattern = input("Enter your regex pattern: ")
instructions = compile_regex(pattern)
print("Инструкции:")
for i in range(len(instructions)):
    print(f'{i}: {instructions[i]}')

v = RegexVM(instructions)
print("Enter your string :")
input = input()
print(v.execute(input))



