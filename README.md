# Language
This language will use korean alphabet. 

| PALAVRA | TRADUÇÃO |
| --- | --- |
| PRINT | 출력하다 |
| IF | 만약~이라면 |
| ELSE | 아니면 |


## EBNF:

```
PROGRAM ::= {STATEMENT};

STATEMENT ::= ASSIGNMENT | PRINT | IF;

ASSIGNMENT ::= IDENTIFIER '=' EXPRESSION;

PRINT ::= '출력하다' '(' EXPRESSION ')';

IF ::= '만약~이라면' EXPRESSION ':' STATEMENT ['아니면' ':' SUITE];

SUITE ::= STATEMENT | '{' {STATEMENT} '}'

EXPRESSION ::= TERM { ( '+' | '-' | '*' | '/' ) TERM };

TERM :== FACTOR {};

FACTOR :==
```
