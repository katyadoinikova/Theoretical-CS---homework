class transition:
    def __init__(self, start_state, symbol, finish_state):
        self.start_state = start_state
        self.symbol = symbol
        self.finish_state = finish_state


class NFA:
    def __init__(self, states_size, alphabet_size, transitions, start, finish):
        self.states_size = states_size
        self.alphabet = alphabet_size
        self.transitions = transitions
        self.start_state = start
        self.finish_state = finish

    def possible_moves(self, symbol, states):
        ans = []
        for state in states:
            for transition in self.transitions:
                if transition.start_state == state and transition.symbol == symbol:
                    ans.append(transition.finish_state)
        return ans

    def do(self, input):
        current_states = self.start_state
        input_int = list(map(int, input.split()))
        for symbol in input_int:
            current_states = self.possible_moves(symbol, current_states)

        for finish_state in self.finish_state:
            if finish_state in current_states:
                return True
        return False


class DFA:
    def __init__(self, states_size, alphabet_size, transitions, start, finish):
        self.states_size = states_size
        self.alphabet = alphabet_size
        self.transitions = transitions
        self.start_state = start
        self.finish_states = finish

    def is_dfa(self):
        if len(self.start_state) != 1:
            return False
        for transition in self.transitions:
            start = transition.start_state
            symbol = transition.symbol
            ans = []
            for transition in self.transitions:
                if transition.start_state == start and transition.symbol == symbol:
                    ans.append(transition.finish_state)
            if len(ans) > 1:
                return False
        return True

    def possible_move(self, symbol, state):
        for transition in self.transitions:
            if transition.start_state == int(state) and transition.symbol == symbol:
                return transition.finish_state

    def do(self, input):
        input_int = list(map(int, input.split()))
        current_state = self.start_state[0]
        for symbol in input_int:
            current_state = self.possible_move(symbol, current_state)
        if current_state in self.finish_states:
            return True
        return False


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


nfa1, dfa1 = file_to_nfa_and_dfa('example.txt')
nfa2, dfa2 = file_to_nfa_and_dfa('example1.txt')

# Tests
assert nfa1.do("0") == True
assert nfa1.do("0 0") == False
assert nfa1.do("1") == False
assert dfa2 != -1
assert dfa2.do("0") == False
assert dfa2.do("0 0") == True
