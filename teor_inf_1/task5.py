from antlr4 import *
from gen.regexLexer import regexLexer
from gen.regexParser import regexParser
from regexInterpreter import RegexInterpreter

def main():
    regex = "(ab*)*"

    lexer = regexLexer(InputStream(regex))
    stream = CommonTokenStream(lexer)
    parser = regexParser(stream)

    tree = parser.regex()
    print("Parse Tree:")
    print(tree.toStringTree(recog=parser))

    interpreter = RegexInterpreter()
    interpreter.visit(tree)

    # Вывод инструкций
    print("Generated instructions:")
    sorted_instr = dict(sorted(interpreter.instructions.items()))
    for key in sorted_instr.keys():
        print(sorted_instr[key])


if __name__ == "__main__":
    main()
