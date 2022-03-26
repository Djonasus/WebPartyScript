# WebPartyScript 2021-2022 By Stas Vasilenko v0.1 INDEV


#include libs
import lexer


COMP = []

def loadstring(string):
    words = lexer.Lex(string)
    print(words)
    print(lexer.Parse(words))

#loadstring("de dew q")
loadstring("style")
