from gen.regexVisitor import regexVisitor
from teor_inf_1.gen.regexParser import regexParser


class RegexInterpreter(regexVisitor):
    def __init__(self):
        self.instructions = {}
        self.instruction_counter = 1

    def visitRegex(self, ctx):
        self.visit(ctx.regex_start())
        self.instructions[self.instruction_counter] = f"{self.instruction_counter} match"

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
                    self.instructions[cur_instruction] = f"{cur_instruction} split {cur_instruction + 1}, {end_instruction + 1}"
                jumps_instruction_numbers.append(self.instruction_counter)
                self.instruction_counter += 1
            for instruction_num in jumps_instruction_numbers:
                self.instructions[instruction_num] = f"{instruction_num} jmp {self.instruction_counter}"
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
                self.instructions[start_instruction] = f"{start_instruction} split {start_instruction + 1}, {self.instruction_counter + 1}"
                self.instructions[self.instruction_counter] = f"{self.instruction_counter} jmp {start_instruction}"
                self.instruction_counter += 1
            elif quantifier == '+':
                start_instruction = self.instruction_counter
                self.visit(ctx.getChild(0))
                self.instructions[self.instruction_counter] = f"{self.instruction_counter} split {start_instruction}, {self.instruction_counter + 1}"
                self.instruction_counter += 1
            elif quantifier == '?':
                start_instruction = self.instruction_counter
                self.instruction_counter += 1
                self.visit(ctx.getChild(0))
                self.instructions[start_instruction] = f"{start_instruction} split {start_instruction + 1}, {self.instruction_counter}"


    def visitParenthesizedExpression(self, ctx:regexParser.ParenthesizedExpressionContext):
        self.visit(ctx.regex_start())

    def visitSymbol(self, ctx:regexParser.SymbolContext):
        self.instructions[self.instruction_counter] = f"{self.instruction_counter} char {ctx.getText()}"
        self.instruction_counter += 1




