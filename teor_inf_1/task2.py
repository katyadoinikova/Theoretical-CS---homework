from task1 import transition, NFA

class DFA_from_NFA:
    def __init__(self, nfa):
        self.nfa = nfa
        self.alphabet = nfa.alphabet
        self.start_state = frozenset(nfa.start_states)
        self.transitions = []
        self.finish_states = set()
        self.states_map = {self.start_state: 0}
        self.next_state_id = 1

    def nfa_to_dfa(self, nfa):
        is_state_visited = []
        is_state_visited.append(self.start_state)
        while len(is_state_visited) != 0:
            cur_dfa_state = is_state_visited.pop()

            for symbol in range(self.alphabet):
                next_nfa_states = nfa.possible_moves(symbol, cur_dfa_state)
                dfa_state = frozenset(next_nfa_states)

                if len(dfa_state) == 0:
                    continue

                if dfa_state not in self.states_map:
                    self.states_map[dfa_state] = self.next_state_id
                    self.next_state_id += 1
                    is_state_visited.append(dfa_state)
                new_transition = transition(self.states_map[cur_dfa_state], symbol, self.states_map[dfa_state])
                self.transitions.append(new_transition)

        for dfa_state in self.states_map:
            if any(state in nfa.finish_states for state in dfa_state):
                self.finish_states.add(self.states_map[dfa_state])

    def possible_move(self, symbol, state):
        for transition in self.transitions:
            if transition.start_state == state and transition.symbol == symbol:
                return transition.finish_state

    def do(self, input):
        input_int = list(map(int, input.split()))
        current_state = list(self.start_state)[0]
        for symbol in input_int:
            current_state = self.possible_move(symbol, current_state)
        if current_state in self.finish_states:
            return True
        return False







