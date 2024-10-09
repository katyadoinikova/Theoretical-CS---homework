from task1 import transition, NFA, DFA
from task2 import DFA_from_NFA

def file_to_nfa_and_dfa(file_name):
    file = open(file_name, 'r')
    states_size = int(file.readline().strip())
    alphabet_size = int(file.readline().strip())

    start = list(map(int, file.readline().strip().split()))
    finish = list(map(int, file.readline().strip().split()))

    transitions = []

    for line in file:
        line.strip()
        split_transition = list(map(int, line.strip().split()))
        if len(split_transition) != 3:
            exit(1)
        cur_transition = transition(split_transition[0], split_transition[1], split_transition[2])
        if cur_transition.start_state > states_size or cur_transition.finish_state > states_size:
            print("States aren't in correct range")
            exit(1)
        if cur_transition.symbol > alphabet_size:
            print("Symbols aren't in correct range")
            exit(1)
        transitions.append(cur_transition)
    nfa = NFA(states_size, alphabet_size, transitions, start, finish)
    dfa = DFA(states_size, alphabet_size, transitions, start, finish)
    if not dfa.is_dfa():
        return (nfa, -1)
    file.close()
    return (nfa, dfa)


def file_output(file_name, dfa):
    f = open(file_name, 'w')
    f.write((str(len(dfa.states_map)) + '\n' + str(dfa.alphabet) + '\n'))
    f.writelines([str(i) + ' ' for i in dfa.start_state])
    f.write('\n')
    f.writelines([str(i) + ' ' for i in dfa.finish_states])
    f.write('\n')
    for transition in dfa.transitions:
        f.write(str(transition.start_state) + ' ' + str(transition.symbol) + ' ' + str(transition.finish_state) + '\n')

    f.close()


nfa1, dfa1 = file_to_nfa_and_dfa('example.txt')
nfa2, dfa2 = file_to_nfa_and_dfa('example1.txt')
nfa3, dfa3 = file_to_nfa_and_dfa('example2.txt')


# Tests
assert nfa1.do("0") == True
assert nfa1.do("0 0 0") == True
assert nfa1.do("0 0") == False
assert nfa1.do("1") == False
assert dfa1 == -1

assert dfa2 != -1
assert dfa2.do("0") == False
assert dfa2.do("0 0") == True

assert nfa3.do("0") == True
assert nfa3.do("0 1 1") == True



dfa4 = DFA_from_NFA(nfa1)
dfa4.nfa_to_dfa(nfa1)
file_output('output.txt', dfa4)

dfa5 = DFA_from_NFA(nfa3)
dfa5.nfa_to_dfa(nfa3)
file_output('output.txt', dfa5)

s = ["0", "0 0", "1", "0 0 0 0", "0 0 1 1 0 0"]
assert (all(nfa1.do(i) == dfa4.do(i) for i in s))

s = ["0", "0 0", "1", "0 0 0 0", "0 0 1 1 0 0"]
assert (all(nfa3.do(i) == dfa5.do(i) for i in s))
