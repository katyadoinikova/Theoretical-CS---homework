from task4 import RegexVM, Instruction, compile_regex





pattern = input("Enter your regex pattern: ")
instructions = compile_regex(pattern)
print("Инструкции:")
for i in range(len(instructions)):
    print(f'{i}: {instructions[i]}')

v = RegexVM(instructions)
print("Enter your string :")
input = input()
print(v.execute(input))



