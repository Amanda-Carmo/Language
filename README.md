# Language
This language will use korean alphabet. 

| PALAVRA | TRADUÇÃO |
| --- | --- |
| PRINT | 출력하다 |
| IF | 만약~이라면 |
| ELSE | 아니면 |
| FUNCTION | 함수 |
| "" | 「」 |



## EBNF:

```
PROGRAM ::= {STATEMENT};

STATEMENT ::= ASSIGNMENT | PRINT | IF | FUNCTION_CALL | FUNCTION_DEFINITION;

ASSIGNMENT ::= IDENTIFIER '=' EXPRESSION;

PRINT ::= '출력하다' '(' EXPRESSION ')';

IF ::= '만약~이라면' EXPRESSION ':' STATEMENT ['아니면' ':' SUITE];

FUNCTION_DEFINITION ::= '함수' IDENTIFIER '(' [PARAMS] ')' ':' SUITE;

PARAMS ::= IDENTIFIER {',' IDENTIFIER};

FUNCTION_CALL ::= IDENTIFIER '(' [ARGS] ')';

ARGS ::= EXPRESSION {' |' EXPRESSION};

SUITE ::= STATEMENT | '{' {STATEMENT} '}';

EXPRESSION ::= TERM { ( '+' | '-' ) TERM };

TERM :== FACTOR {( '*' | '/' | '//' | '%' ) FACTOR};

FACTOR :== IDENTIFIER | NUMBER | STRING | FUNCTION_CALL | FUNCTION_DEFINITION | '(' EXPRESSION ')' | '-' FACTOR | '+' FACTOR;

IDENTIFIER ::= LETTER {LETTER | DIGIT | '_'};

NUMBER ::= DIGIT {DIGIT} ['.' DIGIT {DIGIT}];

DIGIT ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

LETTER ::= [가-힣];

STRING ::= '「' {LETTER | DIGIT | ' ' | '!' | '"' | '#' | '$' | '%' | '&' | '\'' | '(' | ')' | '*' | '+' | ',' | '-' | '.' | '/' | ':' | ';' | '<' | '=' | '>' | '?' | '@' | '[' | '\' | ']' | '^' | '_' | '`' | '{' | '|' | '}' | '~'} '」';

```
