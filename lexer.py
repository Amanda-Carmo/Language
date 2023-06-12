from rply import LexerGenerator
import re

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

        # ignoring whitespace
        self.lexer.ignore(r"\s")

        # Operatorser 
        self.lexer.add('PLUS', r"\+") # Addition
        self.lexer.add('MINUS', r"\-") # Subtraction
        self.lexer.add('MUL', r"\*") # Multiplication
        self.lexer.add('DIV', r"\/") # Division
        self.lexer.add('GREATER', r">") # Greater than
        self.lexer.add('LESS', r"<") # Less than
        self.lexer.add('EQUAL', r"==") # Equal
        self.lexer.add('NOT', r"!") # Not
        self.lexer.add('AND', r'그리고', flags=re.UNICODE) # And
        self.lexer.add('OR', r'또는', flags=re.UNICODE) # Or

        # Delimiters
        self.lexer.add('LPAREN', r"\(") # Left parenthesis
        self.lexer.add('RPAREN', r"\)") # Right parenthesis
        self.lexer.add('COMMA', r",") # Comma

        # Assignment and declaration
        self.lexer.add('ASSIGN', r"\=")
        self.lexer.add('DECLARE', r"::")


        # Reserved keywords
        self.lexer.add('PRINT', r'출력', flags=re.UNICODE) # Print
        self.lexer.add('IF', r'만약', flags=re.UNICODE) # If
        self.lexer.add('ELSE', r'아니면', flags=re.UNICODE) # Else
        self.lexer.add('WHILE', r'동안', flags=re.UNICODE) # While
        self.lexer.add('FUNCTION', r'함수', flags=re.UNICODE) # Function
        self.lexer.add('RETURN', r'반환', flags=re.UNICODE) # Return
        self.lexer.add('END', r'끝', flags=re.UNICODE) # End
        self.lexer.add('TYPE_INT', r'정수', flags=re.UNICODE) # Type int
        self.lexer.add('TYPE_STR', r'문자열', flags=re.UNICODE) # Type string
        self.lexer.add('READ', r'입력', flags=re.UNICODE) # Read input

        # Concatenation
        self.lexer.add('DOT', r"\.") # Dot (concatenation)

        # Newline
        self.lexer.add('NEWLINE', r'%') # Newline

        # Identtifier - hangul and latin alphabet
        self.lexer.add('IDENTIFIER', r'[가-힣a-zA-Z_][_가-힣a-zA-Z_0-9]*')
        
        self.lexer.add('INT', r'\d+') # Integer
        self.lexer.add('STR', r'"[^"]*"') # String

    def get_lexer(self):
        return self.lexer.build()