/* Listing of tokens */
%{
    #include <string>
    #include "parser.tab.hpp"
    #define SAVE_TOKEN yylval.str_val = new std::string(yytext, yyleng)
    #define TOKEN(t) return t
%}

%option noyywrap

%%
[\t\n]                              ; /* Ignore whitespace */
[가-힣a-zA-Z_][가-힣a-zA-Z0-9_]*     SAVE_TOKEN; return IDENTIFIER;
[0-9]+                              SAVE_TOKEN; return INTEGER;

"=="                                return TOKEN(EQ);
"="                                 return TOKEN(ASSIGN);
">"                                 return TOKEN(GT);
"<"                                 return TOKEN(LT);
"::"                                return TOKEN(DECLARATION);           
"("                                 return TOKEN(LPAREN);
")"                                 return TOKEN(RPAREN);
";"                                 return TOKEN(SEMICOLON);
","                                 return TOKEN(COMMA);
"+"                                 return TOKEN(PLUS);
"-"                                 return TOKEN(MINUS);
"*"                                 return TOKEN(MUL);
"/"                                 return TOKEN(DIV);
"."                                 return TOKEN(CONCAT);
"!"                                 return TOKEN(NOT);
"\n"                               return TOKEN(NEWLINE);
"끝"                                return TOKEN(END);
"읽기"                              return TOKEN(READ);
"정수"                              return TOKEN(TYPE);
"문자열"                            return TOKEN(TYPE);
"그리고"                             return TOKEN(AND);
"또는"                               return TOKEN(OR);
"만약~이라면"                        return TOKEN(IF);
"아니면"                             return TOKEN(ELSE);
/* "함수"                              return TOKEN(FUNCTION);
"리턴"                              return TOKEN(RETURN); */
"출력하다"                           return TOKEN(PRINT);
"동안에"                            return TOKEN(WHILE);

[「」] { yylval.str_val = new std::string(yytext+1, yyleng-2); return STRING; }
. { printf("Token desconhecido: %s\n", yytext); }

%%

int yywrap() {
    return 1;
}
