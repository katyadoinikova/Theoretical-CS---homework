# Generated from C:/SP/Theoretical-CS---hw3/teor_inf_1/regex.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
from typing import TextIO

def serializedATN():
    return [
        4,1,8,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,9,2,1,3,
        4,3,29,8,3,11,3,12,3,30,1,4,1,4,3,4,35,8,4,1,4,3,4,38,8,4,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,2,4,42,0,14,
        1,0,0,0,2,17,1,0,0,0,4,19,1,0,0,0,6,28,1,0,0,0,8,34,1,0,0,0,10,39,
        1,0,0,0,12,43,1,0,0,0,14,15,3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,
        18,3,4,2,0,18,3,1,0,0,0,19,24,3,6,3,0,20,21,5,1,0,0,21,23,3,6,3,
        0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,5,1,
        0,0,0,26,24,1,0,0,0,27,29,3,8,4,0,28,27,1,0,0,0,29,30,1,0,0,0,30,
        28,1,0,0,0,30,31,1,0,0,0,31,7,1,0,0,0,32,35,3,12,6,0,33,35,3,10,
        5,0,34,32,1,0,0,0,34,33,1,0,0,0,35,37,1,0,0,0,36,38,7,0,0,0,37,36,
        1,0,0,0,37,38,1,0,0,0,38,9,1,0,0,0,39,40,5,5,0,0,40,41,3,2,1,0,41,
        42,5,6,0,0,42,11,1,0,0,0,43,44,5,7,0,0,44,13,1,0,0,0,4,24,30,34,
        37
    ]

class regexParser ( Parser ):

    grammarFileName = "regex.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'*'", "'+'", "'?'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CHAR", "WS" ]

    RULE_regex = 0
    RULE_regex_start = 1
    RULE_unionExpression = 2
    RULE_concatExpression = 3
    RULE_quantExpression = 4
    RULE_parenthesizedExpression = 5
    RULE_symbol = 6

    ruleNames =  [ "regex", "regex_start", "unionExpression", "concatExpression", 
                   "quantExpression", "parenthesizedExpression", "symbol" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    CHAR=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RegexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regex_start(self):
            return self.getTypedRuleContext(regexParser.Regex_startContext,0)


        def EOF(self):
            return self.getToken(regexParser.EOF, 0)

        def getRuleIndex(self):
            return regexParser.RULE_regex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex" ):
                listener.enterRegex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex" ):
                listener.exitRegex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex" ):
                return visitor.visitRegex(self)
            else:
                return visitor.visitChildren(self)




    def regex(self):

        localctx = regexParser.RegexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_regex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.regex_start()
            self.state = 15
            self.match(regexParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Regex_startContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unionExpression(self):
            return self.getTypedRuleContext(regexParser.UnionExpressionContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_regex_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegex_start" ):
                listener.enterRegex_start(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegex_start" ):
                listener.exitRegex_start(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegex_start" ):
                return visitor.visitRegex_start(self)
            else:
                return visitor.visitChildren(self)




    def regex_start(self):

        localctx = regexParser.Regex_startContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_regex_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.unionExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(regexParser.ConcatExpressionContext)
            else:
                return self.getTypedRuleContext(regexParser.ConcatExpressionContext,i)


        def getRuleIndex(self):
            return regexParser.RULE_unionExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnionExpression" ):
                listener.enterUnionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnionExpression" ):
                listener.exitUnionExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnionExpression" ):
                return visitor.visitUnionExpression(self)
            else:
                return visitor.visitChildren(self)




    def unionExpression(self):

        localctx = regexParser.UnionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unionExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.concatExpression()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 20
                self.match(regexParser.T__0)
                self.state = 21
                self.concatExpression()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(regexParser.QuantExpressionContext)
            else:
                return self.getTypedRuleContext(regexParser.QuantExpressionContext,i)


        def getRuleIndex(self):
            return regexParser.RULE_concatExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatExpression" ):
                listener.enterConcatExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatExpression" ):
                listener.exitConcatExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatExpression" ):
                return visitor.visitConcatExpression(self)
            else:
                return visitor.visitChildren(self)




    def concatExpression(self):

        localctx = regexParser.ConcatExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_concatExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                self.quantExpression()
                self.state = 30 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==7):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuantExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def symbol(self):
            return self.getTypedRuleContext(regexParser.SymbolContext,0)


        def parenthesizedExpression(self):
            return self.getTypedRuleContext(regexParser.ParenthesizedExpressionContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_quantExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuantExpression" ):
                listener.enterQuantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuantExpression" ):
                listener.exitQuantExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantExpression" ):
                return visitor.visitQuantExpression(self)
            else:
                return visitor.visitChildren(self)




    def quantExpression(self):

        localctx = regexParser.QuantExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_quantExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 32
                self.symbol()
                pass
            elif token in [5]:
                self.state = 33
                self.parenthesizedExpression()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                self.state = 36
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParenthesizedExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def regex_start(self):
            return self.getTypedRuleContext(regexParser.Regex_startContext,0)


        def getRuleIndex(self):
            return regexParser.RULE_parenthesizedExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpression" ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesizedExpression(self):

        localctx = regexParser.ParenthesizedExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parenthesizedExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(regexParser.T__4)
            self.state = 40
            self.regex_start()
            self.state = 41
            self.match(regexParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(regexParser.CHAR, 0)

        def getRuleIndex(self):
            return regexParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSymbol" ):
                return visitor.visitSymbol(self)
            else:
                return visitor.visitChildren(self)




    def symbol(self):

        localctx = regexParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(regexParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





