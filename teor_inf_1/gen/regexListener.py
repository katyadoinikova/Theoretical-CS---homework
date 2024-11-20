# Generated from C:/SP/Theoretical-CS---hw3/teor_inf_1/regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .regexParser import regexParser
else:
    from regexParser import regexParser

# This class defines a complete listener for a parse tree produced by regexParser.
class regexListener(ParseTreeListener):

    # Enter a parse tree produced by regexParser#regex.
    def enterRegex(self, ctx:regexParser.RegexContext):
        pass

    # Exit a parse tree produced by regexParser#regex.
    def exitRegex(self, ctx:regexParser.RegexContext):
        pass


    # Enter a parse tree produced by regexParser#regex_start.
    def enterRegex_start(self, ctx:regexParser.Regex_startContext):
        pass

    # Exit a parse tree produced by regexParser#regex_start.
    def exitRegex_start(self, ctx:regexParser.Regex_startContext):
        pass


    # Enter a parse tree produced by regexParser#unionExpression.
    def enterUnionExpression(self, ctx:regexParser.UnionExpressionContext):
        pass

    # Exit a parse tree produced by regexParser#unionExpression.
    def exitUnionExpression(self, ctx:regexParser.UnionExpressionContext):
        pass


    # Enter a parse tree produced by regexParser#concatExpression.
    def enterConcatExpression(self, ctx:regexParser.ConcatExpressionContext):
        pass

    # Exit a parse tree produced by regexParser#concatExpression.
    def exitConcatExpression(self, ctx:regexParser.ConcatExpressionContext):
        pass


    # Enter a parse tree produced by regexParser#quantExpression.
    def enterQuantExpression(self, ctx:regexParser.QuantExpressionContext):
        pass

    # Exit a parse tree produced by regexParser#quantExpression.
    def exitQuantExpression(self, ctx:regexParser.QuantExpressionContext):
        pass


    # Enter a parse tree produced by regexParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:regexParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by regexParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:regexParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by regexParser#symbol.
    def enterSymbol(self, ctx:regexParser.SymbolContext):
        pass

    # Exit a parse tree produced by regexParser#symbol.
    def exitSymbol(self, ctx:regexParser.SymbolContext):
        pass



del regexParser