def Lex(line):
    words = []
    spec_words = ["="," ",",","[","]","(",")","{","}"]
    lastln = 0
    for l in range(len(line)):
        if line[l] in spec_words:
            if l == 0:
                continue
            else:
                words.append(line[lastln:l])
                words.append(line[l])
                lastln = l+1
        elif l == len(line)-1:
            words.append(line[lastln:l+1])
    words = [x for x in words if x]
    return words

def Parse(words):
    result = {}
    for w in range(len(words)):
        if words[w][0] == "#":
             return {"line" : "commentary"}
        else:
            
