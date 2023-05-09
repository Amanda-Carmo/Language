%{
    #include <stdio.h>
    #include <string.h>
    #include "parser.tab.h"

%}

%option noyywrap

%%

[\t\n]                              ; 
[가-힣a-zA-Z_][가-힣a-zA-Z0-9_]*     { return IDENTIFIER; }
[0-9]+                              { return INTEGER; }

"=="                                {return EQ;}
"="                                 {return ASSIGN;}
">"                                 {return GT;}
"<"                                 {return LT;}
"::"                                {return DECLARATION; }          
"("                                 {return LPAREN;}
")"                                 {return RPAREN;}
"+"                                 {return PLUS;}
"-"                                 {return MINUS;}
"*"                                 {return MUL;}
"/"                                 {return DIV;}
"."                                 {return CONCAT;}
"!"                                 {return NOT;}
"\n"                                {return NEWLINE;}
"끝"                                {return END;}
"읽기"                              {return READ;}
"정수"                              {return TYPE;}
"문자열"                            {return TYPE;}
"그리고"                            {return AND;}
"또는"                              {return OR;}
"만약~이라면"                       {return IF;}
"아니면"                            {return ELSE;}
"출력하다"                          {return PRINT;}
"동안에"                            {return WHILE;}

.                                  printf("UNRECOGNIZED TOKEN!\n"); yyterminate();
%%