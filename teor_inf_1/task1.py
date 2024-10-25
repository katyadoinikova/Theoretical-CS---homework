class transition:
    def __init__(self, start_state, symbol, finish_state):
        self.start_state = start_state
        self.symbol = symbol
        self.finish_state = finish_state
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.start_state == other.start_state and self.symbol == other.symbol and self.finish_state == other.finish_state


class NFA:
    def __init__(self, states_size, alphabet_size, transitions, start, finish):
        self.states_size = states_size
        self.alphabet = alphabet_size
        self.transitions = transitions
        self.start_states = start
        self.finish_states = finish

    def possible_moves(self, symbol, states):
        ans = []
        for state in states:
            for transition in self.transitions:
                if transition.start_state == state and transition.symbol == symbol:
                    ans.append(transition.finish_state)
        return ans

    def do(self, input):
        current_states = self.start_states
        input_int = list(map(int, input.split()))
        for symbol in input_int:
            current_states = self.possible_moves(symbol, current_states)

        for finish_state in self.finish_states:
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