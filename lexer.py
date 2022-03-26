spec_s = ["","="," ",",","[","]","(",")","{","}",",",".","\"","\'","/",":",";","+","-","#"]
spec_words = ["div","for","while","and","or","if","else","elseif","style","data", "end", "connect", "include"]


def Lex(line):
    words = []

    lastln = 0
    for l in range(len(line)):
        if line[l] in spec_s:
            if l == 0:
                continue
            else:
                words.append(line[lastln:l])
                words.append(line[l])
                lastln = l+1
        elif l == len(line)-1:
            words.append(line[lastln:l+1])
    words = [x for x in words if x != " "]
    return words

"""def Parse(words):

    result = []
    for w in range(len(words)):
        if words[w][0] == "#":
            break
    """
def Parse(words):
    result = {}
    if words == []: return ()
    if words[0][0] == "#":
        result['construct'] = "commentary"
        return result
    '''
    for w in words:
        if w in spec_words and result["construct"] == None:
            result["construct"] = w
    '''
    if words[0] in spec_words:
        result["construct"] = words[0]
    else:
        result["construct"] = "fun"
    return result
