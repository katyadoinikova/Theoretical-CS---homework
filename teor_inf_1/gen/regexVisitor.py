# Generated from C:/SP/Theoretical-CS---hw3/teor_inf_1/regex.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .regexParser import regexParser
else:
    from regexParser import regexParser

# This class defines a complete generic visitor for a parse tree produced by regexParser.

class regexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by regexParser#regex.
    def visitRegex(self, ctx:regexParser.RegexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#regex_start.
    def visitRegex_start(self, ctx:regexParser.Regex_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#unionExpression.
    def visitUnionExpression(self, ctx:regexParser.UnionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#concatExpression.
    def visitConcatExpression(self, ctx:regexParser.ConcatExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#quantExpression.
    def visitQuantExpression(self, ctx:regexParser.QuantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:regexParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by regexParser#symbol.
    def visitSymbol(self, ctx:regexParser.SymbolContext):
        return self.visitChildren(ctx)



del regexParser