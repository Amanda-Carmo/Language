from rply import ParserGenerator
from comp import (Block, If, While, FuncDec, FuncCall, BinOp, UnOp, 
                  IntVal, StringVal, NoOp, Println, ReturnFunc, Identifier,
                  Assignment, VarDec, Read)

class Parser():
    def __init__(self):
        self.lexer = ParserGenerator(
            # Getting all tokens from lexer.py
            [
                'INT', 'STR', 'IDENTIFIER', 'PLUS', 'MINUS', 'MUL', 'DIV',
                'GREATER', 'LESS', 'EQUAL', 'NOT', 'AND', 'OR', 
                'LPAREN', 'RPAREN', 'COMMA', 'ASSIGN', 'DECLARE', 
                'PRINT', 'IF', 'ELSE', 'WHILE', 'FUNCTION', 'RETURN',
                'END', 'TYPE_INT', 'TYPE_STR', 'READ', 'DOT', 'NEWLINE'
            ]
        )
        
    def parse(self):
        @self.lexer.production('program : block')
        def program(p):
            return p[0] # Block
        
        @self.lexer.production('block : statement')
        def block(p):
            return Block([p[0]])
        
        @self.lexer.production('block : block NEWLINE statement')
        def block(p):
            p[0].add_child(p[2])
            return p[0]
        
        @self.lexer.production('statement : IDENTIFIER DECLARE type ASSIGN relExpression')
        def statement_dec_assign(p):
            if p[2].getstr() == '정수':
                children = [Identifier(p[0].getstr()), p[4]]
            else:
                children = [Identifier(p[0].getstr()), p[4]]
            return VarDec(p[0].getstr(), children)

        @self.lexer.production('statement : IDENTIFIER DECLARE type')
        def statement_dec(p):
            if p[2].getstr() == '정수':
                children = [Identifier(p[0].getstr()), IntVal(0)]
            else:
                children = [Identifier(p[0].getstr()), StringVal('')]    
            return VarDec(p[0].getstr(), children)
        
        @self.lexer.production('statement : IDENTIFIER ASSIGN relExpression')
        def statement_assign(p):
            id = Identifier(p[0].getstr())
            children = [id, p[2]]            
            return Assignment(p[1], children)
        
        @self.lexer.production('statement : IDENTIFIER LPAREN args RPAREN')
        def statement_func_call(p):
            children = p[2]
            return FuncCall(p[0].getstr(), children)
        
        @self.lexer.production('statement : IDENTIFIER LPAREN RPAREN')
        def statement_func_call_empty(p):
            children = []
            return FuncCall(p[0].getstr(), children)
        
        @self.lexer.production('statement : RETURN relExpression')
        def statement_return(p):
            return ReturnFunc(p[0], p[1])
        
        @self.lexer.production('statement : PRINT LPAREN relExpression RPAREN')
        def statement_print(p):
            return Println(p[0], p[2])
        
        @self.lexer.production('statement : IF relExpression NEWLINE block NEWLINE END')
        def statement_if(p):
            child0 = p[1]
            child1 = p[3]
            return If(p[0], [child0, child1])

        @self.lexer.production('statement : IF relExpression NEWLINE block NEWLINE ELSE NEWLINE block NEWLINE END')
        def statement_if_else(p):
            child0 = p[1]
            child1 = p[3]
            child2 = p[7]
            return If(p[0], [child0, child1, child2])
        
        @self.lexer.production('statement : WHILE relExpression NEWLINE block NEWLINE END')
        def statement_while(p):
            children = [p[1], p[3]]
            return While(p[0], children)

        @self.lexer.production('statement : FUNCTION IDENTIFIER LPAREN params RPAREN DECLARE type NEWLINE block NEWLINE END')
        def statement_func_dec(p):
            funcType = p[6].getstr()
            if funcType == '정수':
                funcType = 'Int'
            else:
                funcType = 'Str'
            funcName = (p[1].getstr())
            children = [funcName, p[3], p[8]]

            return FuncDec(funcType, children)
        
        @self.lexer.production('statement : FUNCTION IDENTIFIER LPAREN RPAREN DECLARE type NEWLINE block NEWLINE END')
        def statement_func_dec_empty(p):
            funcType = p[5].getstr()
            if funcType == '정수':
                funcType = 'Int'
            else:
                funcType = 'Str'
            funcName = (p[1].getstr())
            children = [funcName, [], p[7]]

            return FuncDec(funcType, children)
        
        #params
        @self.lexer.production('params : IDENTIFIER DECLARE type')
        def params(p):
            if p[2].getstr() == '정수':
                children = [Identifier(p[0].getstr()), IntVal(0)]
            else:
                children = [Identifier(p[0].getstr()), StringVal('')]
            return [VarDec(p[0].getstr(), children)]
        
        @self.lexer.production('params : params COMMA IDENTIFIER DECLARE type')
        def params(p):
            if p[4].getstr() == '정수':
                children = [Identifier(p[2].getstr()), IntVal(0)]
            else:
                children = [Identifier(p[2].getstr()), StringVal('')]
            p[0].append(VarDec(p[0].getstr(), children))
            return p[0]

        
        @self.lexer.production('relExpression : expression GREATER expression')
        @self.lexer.production('relExpression : expression LESS expression')
        @self.lexer.production('relExpression : expression EQUAL expression')
        def rel_binop(p):
            children = [p[0], p[2]]
            if p[1].gettokentype() == 'GREATER':
                return BinOp('>', children)            
            elif p[1].gettokentype() == 'LESS':
                return BinOp('<', children)            
            elif p[1].gettokentype() == 'EQUAL':
                return BinOp('==', children)            
            else:
                raise AssertionError('Rel BinOp - Unknown operator: %s' % p[1].gettokentype())

        @self.lexer.production('relExpression : expression')
        def rel_expression(p):
            return p[0]
        
        @self.lexer.production('expression : term PLUS term')
        @self.lexer.production('expression : term MINUS term')
        @self.lexer.production('expression : term OR term')
        @self.lexer.production('expression : term DOT term')
        def expression_binop(p):
            children = [p[0], p[2]]
            if p[1].gettokentype() == 'PLUS':
                return BinOp('+', children)            
            elif p[1].gettokentype() == 'MINUS':
                return BinOp('-', children)            
            elif p[1].gettokentype() == 'OR':
                return BinOp('||', children)            
            elif p[1].gettokentype() == 'DOT':                
                return BinOp('.', children)            
            else:
                raise AssertionError('Expression BinOp - Unknown operator: %s' % p[1].gettokentype())
            
        @self.lexer.production('expression : term')
        def expression_term(p):
            return p[0]
        
        @self.lexer.production('term : factor MUL factor')
        @self.lexer.production('term : factor DIV factor')
        @self.lexer.production('term : factor AND factor')
        def term_binop(p):
            children = [p[0], p[2]]
            if p[1].gettokentype() == 'MUL':
                return BinOp('*', children)            
            elif p[1].gettokentype() == 'DIV':
                return BinOp('/', children)            
            elif p[1].gettokentype() == 'AND':
                return BinOp('&&', children)            
            else:
                raise AssertionError('Term BinOp - Unknown operator: %s' % p[1].gettokentype())
            
        @self.lexer.production('term : factor')
        def term_factor(p):
            return p[0]

        @self.lexer.production('factor : INT')
        def factor_int(p):
            return IntVal(p[0].value)
        
        @self.lexer.production('factor : STR')
        def factor_string(p):
            string = (p[0].value).replace('"', '')
            return StringVal(string)
        
        @self.lexer.production('factor : funcCall')
        def factor_func_call(p):
            return p[0]

        @self.lexer.production('factor : IDENTIFIER')
        def factor_identifier(p):
            return Identifier(p[0].getstr())
        
        @self.lexer.production('funcCall : IDENTIFIER LPAREN args RPAREN')
        def func_call(p):
            return FuncCall(p[0].getstr(), p[2])
        
        @self.lexer.production('funcCall : IDENTIFIER LPAREN RPAREN')
        def func_call_empty(p):
            return FuncCall(p[0].getstr(), [])
        
        @self.lexer.production('factor : PLUS factor')
        def factor_plus(p):
            return UnOp('+', [p[1]])
        
        @self.lexer.production('factor : MINUS factor')
        def factor_minus(p):
            return UnOp('-', [p[1]])
        
        @self.lexer.production('factor : NOT factor')
        def factor_not(p):
            return UnOp('!', [p[1]])
        
        @self.lexer.production('factor : LPAREN relExpression RPAREN')
        def factor_paren(p):
            return p[1]
        
        @self.lexer.production('factor : READ LPAREN RPAREN')
        def factor_read(p):
            return Read(p[0].getstr())
        
        # args        
        @self.lexer.production('args : relExpression')
        def args(p):
            return [p[0]]
        
        @self.lexer.production('args : args COMMA relExpression')
        def args(p):
            p[0].append(p[2])
            return p[0]
        
        @self.lexer.production('type : TYPE_INT')
        @self.lexer.production('type : TYPE_STR')
        def type_id(p):
            return p[0]

        @self.lexer.error
        def error_handler(token):
            error_message = f"Erro: Token inesperado '{token.gettokentype()}' na posição {token.source_pos}"
            raise ValueError(error_message) 
        
    def get_parser(self):
        
        return self.lexer.build()