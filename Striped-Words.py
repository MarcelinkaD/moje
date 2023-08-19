# https://py.checkio.org/pl/mission/striped-words/

import re

def checkio(line):
    l = re.split(' |,|_|\.', line)
    nl = []
    akt = ""
    
    for i in l:
        for k in range(len(i)):
            if i[k].isalpha():
                akt += i[k]
            elif i[k].isdigit() and k != 0:
                akt += i[k]
        if len(akt) != 0:
            nl.append(akt)
        akt = ""
    
    sa = set(["a", "e", "i", "o", "u", "y"])
    w = len(nl)
    
    for i in nl:
        if len(i) == 1:
            w -= 1
        else:
            for k in range(1, len(i)):
                if i[k].lower() in sa and i[k - 1].lower() not in sa:
                    pass
                elif i[k].lower() in sa and i[k - 1].lower() in sa:
                    w -= 1
                    break
                elif i[k].lower() not in sa and i[k - 1].lower() not in sa:
                    w -= 1
                    break
            
    return w


print("Example:")
print(checkio("My name is ..."))

# These "asserts" are used for self-checking
assert checkio('1st 2a ab3er root rate') == 1
assert checkio("My name is ...") == 3
assert checkio("Hello world") == 0
assert checkio("A quantity of striped words.") == 1
assert checkio("Dog,cat,mouse,bird.Human.") == 3
assert checkio('For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words.') == 6

print("The mission is done! Click 'Check Solution' to earn rewards!")

