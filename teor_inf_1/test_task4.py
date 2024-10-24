import unittest

from numpy.ma.testutils import assert_equal

from task4 import Instruction, RegexVM, compile_regex


class TextCompileInstructions(unittest.TestCase):
    def test_1(self):
        pattern = 'a'
        instructions = compile_regex(pattern)
        self.assertEqual(instructions[0].operation, 'char')
        self.assertEqual(instructions[1].operation, 'match')

    def test_2(self):
        pattern = 'a|b'
        instructions = compile_regex(pattern)
        self.assertEqual(instructions[0].operation, 'split')
        self.assertEqual(instructions[2].operation, 'jmp')
        self.assertEqual(instructions[4].operation, 'match')

    def test_3(self):
        pattern = 'a*'
        instructions = compile_regex(pattern)
        self.assertEqual(instructions[0].operation, 'split')
        self.assertEqual(instructions[2].operation, 'jmp')
        self.assertEqual(instructions[2].x, 0)
        self.assertEqual(instructions[3].operation, 'match')

class TestExecute(unittest.TestCase):
    def test_1 (self):
        pattern = 'b+a|a|b'
        instructions = compile_regex(pattern)
        v = RegexVM(instructions)
        self.assertEqual(v.execute("ab"), False)
        self.assertEqual(v.execute("bbbbbbba"), True)
        self.assertEqual(v.execute("bbbbbbbaa"), False)

    def test_2 (self):
        pattern = 'a'
        instructions = compile_regex(pattern)
        v = RegexVM(instructions)
        self.assertEqual(v.execute("ab"), False)
        self.assertEqual(v.execute("a"), True)
        self.assertEqual(v.execute("b"), False)

    def test_3 (self):
        pattern = ''
        instructions = compile_regex(pattern)
        v = RegexVM(instructions)
        self.assertEqual(v.execute("a"), False)
        self.assertEqual(v.execute(""), True)
        self.assertEqual(v.execute("b"), False)

    def test_4 (self):
        pattern = 'abab|ab*|b'
        instructions = compile_regex(pattern)
        v = RegexVM(instructions)
        self.assertEqual(v.execute("abab"), True)
        self.assertEqual(v.execute("abbb"), True)
        self.assertEqual(v.execute(""), False)
        self.assertEqual(v.execute("abba"), False)