grammar regex;

regex : regex_start EOF;
regex_start : unionExpression;

unionExpression  : concatExpression ('|' concatExpression)*;
concatExpression : quantExpression+;
quantExpression  : (symbol | parenthesizedExpression) ('*' | '+' | '?')?;

parenthesizedExpression : '(' regex_start ')';
symbol: CHAR;

CHAR : [a-zA-Z0-9];
WS : [ \t\r\n]+ -> skip;
