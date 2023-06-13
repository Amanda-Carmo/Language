from parser_file import Parser
from comp import SymbolTable, FunctionTable
from lexer import Lexer

import re
import sys

def filter(code):
    comment = re.compile(r'#.*')
    # code wothout comments and spaces at the end
    code = (comment.sub('', code)).rstrip()

    # substitute "\n"  with %
    code = re.sub(r'\n', '%', code)

    return code

if __name__ == "__main__":
    if sys.argv[1].rsplit('.', 1)[-1] != '한글':
        print('File must be a .한글 file')
        sys.exit(1)

    with open(sys.argv[1], 'r', encoding="utf8") as f:
        text_input = f.read()

    text_input = filter(text_input) 

    funcTable = FunctionTable()
    symTable = SymbolTable()
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(text_input)

    pg = Parser()
    pg.parse()
    
    parser = pg.get_parser()
    parser.parse(tokens).evaluate(symTable, funcTable)


