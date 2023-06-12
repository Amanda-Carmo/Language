# Used imports
import sys
import re
from rply.token import BaseBox


# _______________Symbol table________________
class SymbolTable:
    def __init__(self):
        self.symbol_table = {}

    # new methods: create for declare a new variable
    # now, the symbol table has a key and a value that is a list with the value and the type of the variable

    def create(self, key, value):
        # Check if variable already exists
        if key in self.symbol_table:
            raise Exception('Variable already exists!')    

        self.symbol_table[key] = value        

    def getter(self, key):
        # print("----------------")
        # print(self.symbol_table[key])
        return self.symbol_table[key]
    
    def setter(self, key, value):
        # Check if variable was not created - cant atribuite a value to a variable that was not declared.
        if key not in self.symbol_table:
            raise Exception('Variable not declared!')
        
        # Check if the type of the variable is the same of the value
        if(self.symbol_table[key][0] == value[0]):
            self.symbol_table[key] = value

        else:
            raise Exception('Invalid type!')


# ________________Function table____________________
class FunctionTable:
    def __init__(self):
        self.table = {}


    def create(self, key, value):
        if(key in self.table.keys()):
            raise Exception("variable cannot be redeclared")
        
        self.table[key] = value       

    def getter(self, key):
        return self.table[key]
    
    
    def setter(self, key, value):
        # Check if variable was not created - cant atribuite a value to a variable that was not declared.
        if key not in self.table:
            raise Exception('Variable not declared!')
            
        self.table[key] = value

# _____________________NODE______________________
class Node(BaseBox):
    def __init__(self, value, children):
        self.value = value # variant
        self.children = children # list of nodes

    def evaluate(self, symbolTable, funcTable):
        pass


# ___________________FuncDec_____________________
class FuncDec(BaseBox):
    def __init__(self, value, children):
        self.value = value # type
        self.children = children # ident, args (VarDecs) and block

    def evaluate(self, symbolTable, funcTable):
        funcTable.create(self.children[0], self)
        funcTable.setter(self.children[0], self)
        # print(f"funcd: {funcTable.table}")


# ___________________FuncCall_____________________
class FuncCall(BaseBox):
    def __init__(self, value, children):
        self.value = value 
        self.children = children
        self.FuncST = SymbolTable()


    def evaluate(self, symbolTable, funcTable):
        func = funcTable.getter(self.value) # get the FuncDec from the FuncTable
        # get the fundec type
        funcType = func.value

        # Checking if the number of arguments is the same of the number of parameters
        if len(self.children) == len(func.children[1]):
            
            if len(self.children) == 0:
                # retorna o Block do FuncDec c/ a nova ST
                block = func.children[2].evaluate(self.FuncST, funcTable)
                if funcType == block[0]:
                    return block    
                else:
                    raise Exception("Invalid return type!")
            
            else:
                for i in range(len(self.children)):
                    # print("Children:")
                    # print(func.children[1][i])
                    # children[1] is a list of VarDecs, doing evaluate to create the variables in the new ST
                    func.children[1][i].evaluate(self.FuncST, funcTable)
                    # atribute the args to the parameters
                    eval2 = self.children[i].evaluate(symbolTable, funcTable)
                    self.FuncST.setter(func.children[1][i].value, eval2) 

                # return Block from FuncDec with new ST
                block = func.children[2].evaluate(self.FuncST, funcTable)
                # print(f"test1 {self.FuncST}")
                # print(f"test2 {symbolTable.symbol_table}")
                if funcType == block[0]:
                    return block
                
                else:
                    raise Exception("Invalid return type!")
        
        else:
            raise Exception("Invalid number of arguments!")


#______________________BINOP_____________________
class BinOp(BaseBox):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable, funcTable):
        if self.value == '+':
            # print(self.children[0].evaluate(symbolTable, funcTable))

            # Check if both children are numbers
            if (self.children[0].evaluate(symbolTable, funcTable)[0] == 'Int') and (self.children[1].evaluate(symbolTable, funcTable)[0] == 'Int'):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], (self.children[0].evaluate(symbolTable, funcTable)[1] + self.children[1].evaluate(symbolTable, funcTable)[1])]
            
            else:
                raise Exception('Both children must be same type!')
        
        elif self.value == '-':          
            # Check if both children are numbers
            if ((self.children[0].evaluate(symbolTable, funcTable)[0] == 'Int') and (self.children[1].evaluate(symbolTable, funcTable)[0] == 'Int')):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], int(self.children[0].evaluate(symbolTable, funcTable)[1]) - int(self.children[1].evaluate(symbolTable, funcTable)[1])]
            else:
                raise Exception('Both children must be numbers!')
        
        elif self.value == '*':
            # Check if both children are numbers
            if (self.children[0].evaluate(symbolTable, funcTable)[0] == 'Int') and (self.children[1].evaluate(symbolTable, funcTable)[0] == 'Int'):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], int(self.children[0].evaluate(symbolTable, funcTable)[1]) * int(self.children[1].evaluate(symbolTable, funcTable)[1])]
            else:
                raise Exception('Both children must be numbers!')
        
        elif self.value == '/':
            # Check if both children are numbers
            if (self.children[0].evaluate(symbolTable, funcTable)[0] == 'Int') and (self.children[1].evaluate(symbolTable, funcTable)[0] == 'Int'):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], int(self.children[0].evaluate(symbolTable, funcTable)[1]) // int(self.children[1].evaluate(symbolTable, funcTable)[1])]
            else:
                raise Exception('Both children must be numbers!')
        
        elif self.value == '&&':
            if (self.children[0].evaluate(symbolTable, funcTable)[0] == self.children[1].evaluate(symbolTable, funcTable)[0]):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], int(int(self.children[0].evaluate(symbolTable, funcTable)[1]) and int(self.children[1].evaluate(symbolTable, funcTable)[1]))]
            else:
                raise Exception('Both children must be boolean!')
        
        elif self.value == '||':
            if (self.children[0].evaluate(symbolTable, funcTable)[0] == self.children[1].evaluate(symbolTable, funcTable)[0]):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], int(int(self.children[0].evaluate(symbolTable, funcTable)[1]) or int(self.children[1].evaluate(symbolTable, funcTable)[1]))]
            else:
                raise Exception('Both children must be boolean!')

        elif self.value == '>':            
            if (self.children[0].evaluate(symbolTable, funcTable)[0] == self.children[1].evaluate(symbolTable, funcTable)[0]):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], int(int(self.children[0].evaluate(symbolTable, funcTable)[1]) > int(self.children[1].evaluate(symbolTable, funcTable)[1]))]
            # return self.children[0].evaluate(symbolTable, funcTable) > self.children[1].evaluate(symbolTable, funcTable)
            else:
                raise Exception('Both children must be numbers!')
        
        elif self.value == '<':
            if (self.children[0].evaluate(symbolTable, funcTable)[0] == self.children[1].evaluate(symbolTable, funcTable)[0]):
                return [self.children[0].evaluate(symbolTable, funcTable)[0], int(int(self.children[0].evaluate(symbolTable, funcTable)[1]) < int(self.children[1].evaluate(symbolTable, funcTable)[1]))]
            # return self.children[0].evaluate(symbolTable, funcTable) < self.children[1].evaluate(symbolTable, funcTable)
            else:
                raise Exception('Both children must be numbers!')

        elif self.value == '==':
            return [self.children[0].evaluate(symbolTable, funcTable)[0], int(int(self.children[0].evaluate(symbolTable, funcTable)[1]) == int(self.children[1].evaluate(symbolTable, funcTable)[1]))]
            # else:
            #     raise Exception('Both children must be numbers!')
            # return self.children[0].evaluate(symbolTable, funcTable) == self.children[1].evaluate(symbolTable, funcTable)


        elif self.value == ".":
            return['Str',str(str(self.children[0].evaluate(symbolTable, funcTable)[1]) + str(self.children[1].evaluate(symbolTable, funcTable)[1]))]


#______________________UNOP______________________
class UnOp(BaseBox):
    def  __init__(self, value, children):
        self.value = value # variant
        self.children = children # list of BaseBoxs

    def evaluate(self, symbolTable, funcTable):
        if self.value == '-':
            return [self.children[0].evaluate(symbolTable, funcTable)[0], -self.children[0].evaluate(symbolTable, funcTable)]
        
        elif self.value == '!':
            return [self.children[0].evaluate(symbolTable, funcTable)[0], int(not(self.children[0].evaluate(symbolTable, funcTable)[1]))]
        
        return [self.children[0].evaluate(symbolTable, funcTable)[0], self.children[0].evaluate(symbolTable, funcTable)]

#______________________INTVAL_____________________
class IntVal(BaseBox):

    def __init__(self, value):
        self.value = value # variant

    def evaluate(self, symbolTable, funcTable):
        return ['Int', self.value]
    
#______________________STRINGVAL____________________
class StringVal(BaseBox):
    def __init__(self, value):
        self.value = value 

    def evaluate(self, symbolTable, funcTable):
        return ['Str', self.value]
    
#________________________NOOP______________________
class NoOp(BaseBox):
    def __init__(self, value):
        self.value = value

    def evaluate(self, symbolTable, funcTable):
        pass

#_______________________PRINTLN_____________________
class Println(BaseBox):
    def __init__(self, value, child):
        self.value = value
        self.child = child

    def evaluate(self, symbolTable, funcTable):
        eval = self.child.evaluate(symbolTable, funcTable)[1]
        print(eval)


#_____________________RETURN_______________________
class ReturnFunc(BaseBox):
    def __init__(self, value, child):
        self.value = value
        self.child = child

    def evaluate(self, symbolTable, funcTable):
        # check if type of return is the same as the function type 
        # print(f"ret: {self.child}")
        eval = self.child.evaluate(symbolTable, funcTable)
        # print(f"ret1{eval}")
        return eval

# __________________IDENTIFIER____________________

class Identifier(BaseBox):
    def __init__(self, value):
        self.value = value # key name - variable
    
    # get from symbol table the value of the identifier
    def evaluate(self, symbolTable, funcTable):
        # Getter: get the value of the identifier from the symbol table
        # pass the key as argumrnt
        # print(symbolTable.getter(self.value))
        return symbolTable.getter(self.value)
        

# ___________________Assignment___________________
class Assignment(BaseBox):
    def __init__(self, value, children):
        # Value is a list with type and value
        self.value = value
        self.children = children # identifier and relexpression

    def evaluate(self, symbolTable, funcTable):
        eval1 = self.children[0].value
        eval2 = self.children[1].evaluate(symbolTable, funcTable)
        # Setter: set the value of the identifier in the symbol table
        symbolTable.setter(eval1, eval2)


# ____________________VARDEC_______________________
class VarDec(BaseBox):
    def __init__(self, value, children):
        self.value = value
        self.children = children # identifier and type

    def evaluate(self, symbolTable, funcTable):
        # Create a new variable in the symbol table
        # print(f"var: {self.children[0].value}")
        if type(self.children[1].value) == int:
            tupla1 = self.children[1].evaluate(symbolTable, funcTable)
            # print(tupla1)
            symbolTable.create(self.children[0].value, tupla1)

        else:
            tupla2 = self.children[1].evaluate(symbolTable, funcTable)
            # print(tupla2)
            symbolTable.create(self.children[0].value, tupla2)


#______________________BLOCK______________________
class Block(BaseBox):
    def __init__(self, children):
        self.children = children

    def add_child(self, child):
        self.children.append(child)

    def evaluate(self, symbolTable, funcTable):
        for child in self.children:
            eval = child.evaluate(symbolTable, funcTable)
            if eval is not None:
                return eval
        
# ____________________READ__________________________
class Read(BaseBox):
    def __init__(self, value):
        self.value = value

    def evaluate(self, symbolTable, funcTable):
        # read from stdin
        input_val = input()
        return (['Int', int(input_val)])
    

# ____________________IF__________________________
class If(BaseBox):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable, funcTable):
        eval = self.children[0].evaluate(symbolTable, funcTable)[1]
        # If evaluate of the first child is true, evaluate the second child
        if eval:
            self.children[1].evaluate(symbolTable, funcTable)
        
        # If evaluate of the first child is false and there is a third child, evaluate it
        elif len(self.children) == 3:
            self.children[2].evaluate(symbolTable, funcTable)


# ____________________WHILE__________________________
class While(BaseBox):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, symbolTable, funcTable):
        # while evaluate of the first child is true, evaluate the second child
        
        while self.children[0].evaluate(symbolTable, funcTable)[1]:
            self.children[1].evaluate(symbolTable, funcTable)