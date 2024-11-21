from task4 import RegexVM, Instruction, compile_regex
from antlr4 import *
from gen.regexLexer import regexLexer
from gen.regexParser import regexParser
from task5 import RegexInterpreter, compile_regex
from Errors import CustomErrorListener

def main():
    regex = input("Enter your regex pattern: ")
    instructions = compile_regex(regex)

    print("Generated instructions:")
    for i in range(len(instructions)):
        print(f'{i}: {instructions[i]}')

    v = RegexVM(instructions)
    print("Enter your string :")
    input_str = input()
    print(v.execute(input_str))




if __name__ == "__main__":
    main()




