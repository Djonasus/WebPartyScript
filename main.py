# WebPartyScript 2021 By Stas Vasilenko v0.1 INDEV


#include libs
import lexer
import parser


COMP = []

def loadstring(string):
    words = lexer.Lex(string)
    print(words)
    #parser.Parse(words)
