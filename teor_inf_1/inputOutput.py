from task1 import transition, NFA, DFA


def file_to_nfa_and_dfa(file_name):
    file = open(file_name, 'r')
    states_size = int(file.readline().strip())
    alphabet_size = int(file.readline().strip())

    start = list(map(int, file.readline().strip().split()))
    finish = set(map(int, file.readline().strip().split()))

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
        return nfa, -1
    file.close()
    return nfa, dfa


def file_output(file_name, dfa):
    f = open(file_name, 'w')
    f.write((str(len(dfa.states_map)) + '\n' + str(dfa.alphabet) + '\n'))
    f.write(str(dfa.start_state) + '\n')
    f.writelines([str(i) + ' ' for i in dfa.finish_states])
    f.write('\n')
    for transition in dfa.transitions:
        f.write(str(transition.start_state) + ' ' + str(transition.symbol) + ' ' + str(transition.finish_state) + '\n')

    f.close()