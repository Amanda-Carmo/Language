%{
    #include<stdio.h> 
    
    extern int yylex();
    void yyerror(const char *s) { printf("ERROR: %s\n", s); } 
%}


/* Definindo tokens */
%token IDENTIFIER INTEGER STRING
%token IF ELSE WHILE END TYPE PRINT READ DECLARATION
%token PLUS MINUS MUL DIV CONCAT
%token EQ LT GT NOT AND OR ASSIGN
%token LPAREN RPAREN NEWLINE

%start block

%%

block :  statement
        ;

statement : vardec
            | assignment
            | if
            | while
            | print
            
            NEWLINE
            ;

relexpression: expression LT expression
                | expression GT expression
                | expression EQ expression
                | expression CONCAT expression
                | expression
                ;

expression : term PLUS term
            | term MINUS term
            | term OR term
            | term
            ;

term : factor
        | factor MUL factor
        | factor DIV factor
        | factor AND factor
        ;

factor: INTEGER
        | STRING
        | IDENTIFIER
        | NOT factor
        | PLUS factor
        | MINUS factor
        | READ LPAREN RPAREN
        | LPAREN relexpression RPAREN
        ;

assignment: TYPE IDENTIFIER ASSIGN relexpression;

vardec: IDENTIFIER DECLARATION TYPE;

if: IF relexpression block else;

else: ELSE block END | END;

while: WHILE relexpression block END;

print: PRINT LPAREN relexpression RPAREN;

%%

int yyparse();