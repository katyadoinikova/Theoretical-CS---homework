from gen.regexVisitor import regexVisitor
from teor_inf_1.gen.regexParser import regexParser
from task4 import Instruction
from antlr4 import *
from gen.regexLexer import regexLexer
from gen.regexParser import regexParser
from Errors import CustomErrorListener


class RegexInterpreter(regexVisitor):
    def __init__(self):
        self.instructions = {}
        self.instruction_counter = 0

    def visitRegex(self, ctx):
        self.visit(ctx.regex_start())
        self.instructions[self.instruction_counter] = Instruction('match')

    def visitRegex_start(self, ctx:regexParser.Regex_startContext):
        self.visit(ctx.unionExpression())

    def visitUnionExpression(self, ctx):
        branches = ctx.concatExpression()
        jumps_instruction_numbers = []
        if len(branches) > 1:
            for i in range(len(branches)):
                cur_instruction = self.instruction_counter
                if i != len(branches) - 1:
                    self.instruction_counter += 1
                self.visit(branches[i])
                end_instruction = self.instruction_counter
                if i != len(branches) - 1:
                    self.instructions[cur_instruction] = Instruction('split', cur_instruction + 1, end_instruction + 1)
                jumps_instruction_numbers.append(self.instruction_counter)
                self.instruction_counter += 1
            for instruction_num in jumps_instruction_numbers:
                self.instructions[instruction_num] = Instruction('jmp', self.instruction_counter)
        else:
            self.visit(branches[0])

    def visitConcatExpression(self, ctx):
        for child in ctx.quantExpression():
            self.visit(child)

    def visitQuantExpression(self, ctx:regexParser.QuantExpressionContext):
        if ctx.symbol() and ctx.getChildCount() == 1:
            self.visit(ctx.symbol())
        elif ctx.parenthesizedExpression() and ctx.getChildCount() == 1:
            self.visit(ctx.parenthesizedExpression())
        elif ctx.getChildCount() > 1:
            quantifier = ctx.getChild(1).getText()
            if quantifier == '*':
                start_instruction = self.instruction_counter
                self.instruction_counter += 1
                self.visit(ctx.getChild(0))
                self.instructions[start_instruction] = Instruction('split', start_instruction + 1, self.instruction_counter + 1)
                self.instructions[self.instruction_counter] = Instruction('jmp', start_instruction)
                self.instruction_counter += 1
            elif quantifier == '+':
                start_instruction = self.instruction_counter
                self.visit(ctx.getChild(0))
                self.instructions[self.instruction_counter] = Instruction('split', start_instruction, self.instruction_counter + 1)
                self.instruction_counter += 1
            elif quantifier == '?':
                start_instruction = self.instruction_counter
                self.instruction_counter += 1
                self.visit(ctx.getChild(0))
                self.instructions[start_instruction] = Instruction('split', start_instruction + 1, self.instruction_counter)


    def visitParenthesizedExpression(self, ctx:regexParser.ParenthesizedExpressionContext):
        self.visit(ctx.regex_start())

    def visitSymbol(self, ctx:regexParser.SymbolContext):
        self.instructions[self.instruction_counter] = Instruction('char', ctx.getText())
        self.instruction_counter += 1

def compile_regex(regex):
    lexer = regexLexer(InputStream(regex))
    error_listener = CustomErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    parser = regexParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.regex()
    if error_listener.errors:
        for error in error_listener.errors:
            print(error)
        return

    interpreter = RegexInterpreter()
    interpreter.visit(tree)

    sorted_instr = dict(sorted(interpreter.instructions.items()))
    instructions = []
    for key in sorted_instr.keys():
        instructions.append(sorted_instr[key])
    return instructions