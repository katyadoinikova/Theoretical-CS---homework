from collections import deque, defaultdict

from task1 import transition, NFA, DFA

def get_reachable_dfa(dfa):
    reachable_states = []
    queue = {dfa.start_state}

    while queue:
        state = queue.pop()
        reachable_states.append(state)
        for symbol in range(dfa.alphabet):
            for transition_ in dfa.transitions:
                if transition_.start_state == state and transition_.symbol == symbol:
                    if transition_.finish_state not in reachable_states:
                        queue.add(transition_.finish_state)

    set_for_new_states = {}
    for i in range(len(reachable_states)):
        set_for_new_states[reachable_states[i]] = i

    new_transitions = []
    for transition_ in dfa.transitions:
        if transition_.start_state in reachable_states and transition_.finish_state in reachable_states:
            new_transition = transition(set_for_new_states[transition_.start_state], transition_.symbol,
                              set_for_new_states[transition_.finish_state])
            new_transitions.append(new_transition)

    new_finish = []
    for finish_state in dfa.finish_states:
        if finish_state in reachable_states:
            new_finish.append(set_for_new_states[finish_state])

    return DFA(len(reachable_states), dfa.alphabet, new_transitions, set_for_new_states[dfa.start_state], new_finish)


def minimize(dfa):
    reachable_dfa = get_reachable_dfa(dfa)
    states = []
    alphabet = []
    for i in range(reachable_dfa.states_size):
        states.append(i)
    for i in range(reachable_dfa.alphabet):
        alphabet.append(i)

    cur_partition = [frozenset(reachable_dfa.finish_states), frozenset(set(states) - set(reachable_dfa.finish_states))]

    while True:
        new_partition = []
        for fragment in cur_partition:
            new_fragments = defaultdict(set)
            for state in fragment:
                transition_for_state = []
                for symbol in alphabet:
                    for transition_ in reachable_dfa.transitions:
                        if transition_.start_state == state and transition_.symbol == symbol:
                            for i in range(len(cur_partition)):
                                if transition_.finish_state in cur_partition[i]:
                                    transition_for_state.append(i)
                new_fragments[tuple(transition_for_state)].add(state)

            for i in new_fragments.keys():
                states_in_partition = []
                for state in new_fragments[i]:
                    states_in_partition.append(state)
                new_partition.append(frozenset(states_in_partition))

        if len(new_partition) == len(cur_partition):
            break
        cur_partition = new_partition

    min_transitions = {}
    partition_to_states = {}
    min_start_state = None
    min_finish_states = set()
    i = 0
    for fragment in cur_partition:
        partition_to_states[fragment] = i
        i+=1

    for fragment in cur_partition:
        if reachable_dfa.start_state in fragment:
            min_start_state = partition_to_states[fragment]
        is_finish_state = False
        for state in fragment:
            if state in reachable_dfa.finish_states:
                is_finish_state = True
                break
        if is_finish_state:
            min_finish_states.add(partition_to_states[fragment])
        for state in fragment:
            for symbol in alphabet:
                next_state = -1
                for transition_ in reachable_dfa.transitions:
                    if transition_.start_state == state and transition_.symbol == symbol:
                        for finish_fragment in cur_partition:
                            if transition_.finish_state in finish_fragment:
                                next_state = partition_to_states[finish_fragment]
                                break
                if next_state != -1:
                    for next_fragment in cur_partition:
                        if next_state in next_fragment:
                            new_transition = transition(partition_to_states[fragment], symbol, next_state)
                            min_transitions[(partition_to_states[fragment], symbol)] = new_transition

    min_transitions_arr = []
    for j in min_transitions.values():
        min_transitions_arr.append(j)

    return DFA(i, reachable_dfa.alphabet, min_transitions_arr, min_start_state, min_finish_states)


def equivalent(dfa1, dfa2):
    min_dfa1 = minimize(dfa1)
    min_dfa2 = minimize(dfa2)

    if min_dfa1.states_size != min_dfa2.states_size:
        return False
    if min_dfa1.alphabet != min_dfa2.alphabet:
        return False

    queue = deque([(min_dfa1.start_state, min_dfa2.start_state)])
    visited = {min_dfa1.start_state: min_dfa2.start_state}

    while queue:
        state_1, state_2 = queue.popleft()
        if (state_1 in min_dfa1.finish_states) != (state_2 in min_dfa2.finish_states):
            return False

        for symbol in range(min_dfa1.alphabet):
            next_state1 = -1
            for transition_ in min_dfa1.transitions:
                if transition_.start_state == state_1 and transition_.symbol == symbol:
                    next_state1 = transition_.finish_state
                    break
            next_state2 = -1
            for transition_ in min_dfa2.transitions:
                if transition_.start_state == state_2 and transition_.symbol == symbol:
                    next_state2 = transition_.finish_state
                    break

            if (next_state1 == -1 and next_state2 != -1) or (next_state1 != -1 and next_state2 == -1) :
                return False

            if next_state1 not in visited.keys():
                visited[next_state1] = next_state2
                queue.append((next_state1, next_state2))
            else:
                if visited[next_state1] != next_state2:
                    return False

    return True



def accepts_all(dfa):
    min_dfa = minimize(dfa)
    if min_dfa.states_size == 1 and 0 in min_dfa.finish_states:
        return True
    return False


