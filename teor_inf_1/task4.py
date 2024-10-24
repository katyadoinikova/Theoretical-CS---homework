class Instruction:
    def __init__(self, op, x=None, y=None):
        self.operation = op
        self.x = x
        self.y = y

    def __repr__(self):
        if self.operation == 'char':
            return f'char {self.x}'
        elif self.operation == 'match':
            return 'match'
        elif self.operation == 'jmp':
            return f'jmp {self.x}'
        elif self.operation == 'split':
            return f'split {self.x}, {self.y}'


class RegexVM:
    def __init__(self, instructions):
        self.instructions = instructions

    def execute(self, string):
        states = [(0, 0)]  # (program_counter, string_index)

        while states:
            pc, si = states.pop()
            if pc >= len(self.instructions):
                continue

            inst = self.instructions[pc]

            if inst.operation == 'char':
                if si < len(string) and string[si] == inst.x:
                    states.append((pc + 1, si + 1))
            elif inst.operation == 'match' and si == len(string):
                return True
            elif inst.operation == 'jmp':
                states.append((inst.x, si))
            elif inst.operation == 'split':
                states.append((inst.x, si))
                states.append((inst.y, si))

        return False




def compile_regex(pattern):
    instructions = {}
    cur_index_pos = 0
    cur_index_neg = -1
    for i in range(len(pattern)):
        if pattern[i] == 'a' or pattern[i] == 'b':
            instructions[cur_index_pos] = Instruction('char', pattern[i])
            cur_index_pos+=1
        elif pattern[i] == '*':
            split_inst = Instruction('split', cur_index_pos, cur_index_pos + 2)
            instructions[cur_index_pos] = instructions[cur_index_pos - 1]
            instructions[cur_index_pos - 1] = split_inst
            instructions[cur_index_pos + 1] = Instruction('jmp', cur_index_pos - 1)
            cur_index_pos = cur_index_pos + 2
        elif pattern[i] == '+':
            split_inst = Instruction('split', cur_index_pos - 1, cur_index_pos + 1)
            instructions[cur_index_pos] = split_inst
            cur_index_pos += 1
        elif pattern[i] == '?':
            split_inst = Instruction('split', cur_index_pos, cur_index_pos + 1)
            instructions[cur_index_pos] = instructions[cur_index_pos - 1]
            instructions[cur_index_pos - 1] = split_inst
            cur_index_pos += 1
        elif pattern[i] == '|':
            split_inst = Instruction('split', cur_index_neg + 1, cur_index_pos + 1)
            instructions[cur_index_neg] = split_inst
            instructions[cur_index_pos] = Instruction('jmp', -1)
            cur_index_pos +=1
            cur_index_neg -= 1
        i += 1
    instructions[cur_index_pos] = Instruction('match')
    for i in sorted(instructions.keys()):
        if instructions[i].operation == 'jmp' and instructions[i].x == -1:
            instructions[i].x = cur_index_pos
    corrected_num_instr = []
    cur_index_neg += 1
    for i in sorted(instructions.keys()):
        if instructions[i].operation == 'jmp' or instructions[i].operation == 'split':
            instructions[i].x -= cur_index_neg
        if instructions[i].operation == 'split':
            instructions[i].y -= cur_index_neg
        corrected_num_instr.append(instructions[i])
    return corrected_num_instr



