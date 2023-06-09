# Language
This language is based on Julia language, but some reserved words use korean alphabet, **Hangul**. 

| PALAVRA | TRADUÇÃO |
| --- | --- |
| PRINT | 출력하다 |
| Read | 읽기 |
| IF | 만약 |
| ELSE | 아니면 |
| WHILE | 동안에 |
| FUNCTION | 함수 |
| RETURN | 반환 |
| END | 끝 |
| AND | 그리고 |
| OR | 그리고 |
| Int| 정수
| Str | 문자열


## EBNF:

```
PROGRAM ::= BLOCK

BLOCK ::= STATEMENT '\n' | BLOCK STATEMENT

STATEMENT ::= ASSIGNMENT | DECLARATION | FUNCTION_CALL| RETURN | PRINT | IF | WHILE | FUNCTION_DEFINITION | 

DECLARATION ::= IDENTIFIER '::' TYPE;

ASSIGNMENT ::= IDENTIFIER '=' RELEXPRESSION;

PRINT ::= '출력하다' '(' RELEXPRESSION ')';

IF ::= '만약' RELEXPRESSION '\n' BLOCK '끝' | '만약' RELexpression '\n' BLOCK '아니면' BLOCK '끝';

WHILE ::= '동안에' RELEXPRESSION '\n' BLOCK '끝';

FUNCTION_DEFINITION ::= '함수' IDENTIFIER '(' [PARAMS] ')' '\n' BLOCK '끝'; | '함수' IDENTIFIER '(' [PARAMS] ')' '\n' BLOCK '반환' RELEXPRESSION '끝';

PARAMS ::= IDENTIFIER ',' PARAMS | IDENTIFIER | ε;

FUNCTION_CALL ::= IDENTIFIER '(' [ARGS] ')';

ARGS ::= RELEXPRESSION ',' ARGS | RELEXPRESSION | ε;

RELEXPRESSION ::= EXPRESSION { ( '==' | '>' | '<' ) EXPRESSION };

EXPRESSION ::= TERM {( '+' | '-' | '그리고' | '.' ) TERM};

TERM :== FACTOR {( '*' | '/' | '또는' ) FACTOR};

FACTOR :== INT | STRING | IDENTIFIER | FUNCTION_CALL |  '(' EXPRESSION ')' | '-' FACTOR | '+' FACTOR | '!' FACTOR | 읽기 '(' ')';

FUNCTION_CALL ::= IDENTIFIER '(' [ARGS] ')';

IDENTIFIER ::= LETTER {LETTER | DIGIT | '_'};

NUMBER ::= DIGIT {DIGIT} ['.' DIGIT {DIGIT}];

DIGIT ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

LETTER ::= [가-힣a-zA-Z_][_가-힣a-zA-Z_0-9]*;

STRING ::= '「' {LETTER | DIGIT | ' ' | '!' | '"' | '#' | '$' | '%' | '&' | '\'' | '(' | ')' | '*' | '+' | ',' | '-' | '.' | '/' | ':' | ';' | '<' | '=' | '>' | '?' | '@' | '[' | '\' | ']' | '^' | '_' | '`' | '{' | '|' | '}' | '~'} '」';

```

## Tests examples:

The following examples show the use of the language and some of its features.

- Below, is shown how the declaration of variables is done. It is very similar to the Julia language, but the reserved words `Int` and `String` are replaced by the Hangul alphabet. Also, it ispossible to see the reserved word `출력` being used to print the concatenation of `B` and `A`.
We can concatenate both strings and integers with the `.` operator.
The output after running the code is "`ab12`".


``` julia
B::문자열
B = "ab"
A::정수 
A = 12
출력(B.A)
```
- The example below shows the use of `동안`, that is the translation for `while`. The output after running the code is:
    ``` text
    8 
    4
    2
    ```

```julia
B::정수 
B = 16
A::정수 
A = 2
동안 A < B
    B = B / 2
    출력(B)
끝
```
- Next, `만약` (`if`) was added to the previous example. If true, the code will print "`B는 4입니다.`", if false, "`B는 4가 아닙니다`" will be printed. The output after running the code is:
    ``` text

    8
    B는 4가 아닙니다.
    4
    B는 4입니다.
    2
    B는 4가 아닙니다.
    ```
    As the julia language, after using `만약` (`if`), it is possible to use `아니면` (`else`). Then, the token `끝` (`end`) is used to close the `만약` (`if`).

```julia
B::정수 
B = 16
A::정수 
A = 2
동안 A < B
    B = B / 2
    출력(B)
    만약 (B == 4)
        출력("B는 4입니다.")
    아니면
        출력("B는 4가 아닙니다.")
    끝    
끝
```

- The example below shows the use of `함수` (`function`). The output after running the code is:
    ``` text
    4
    8
    ```

```julia
B::정수
B = 입력()
출력(B)
함수 a_x (B::정수) :: 정수
    반환 (B * 2)
끝
A::정수 = a_x(B)
출력(A)
```
