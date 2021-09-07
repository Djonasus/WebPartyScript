# WebPartyScript 2021 By Stas Vasilenko v0.1 INDEV


#include libs
import lexer


COMP = []

def loadstring(string):
    words = lexer.Lex(string)
    #print(words)
    print(lexer.Parse(words))

loadstring("#print('hello')")
