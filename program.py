# https://szkopul.edu.pl/problemset/problem/jvPBZm53yfvDkYKuuxbQvjNe/site/?key=statement

from sys import stdin
input = stdin.readline

def czy_poprawne(s, otw):
    stos = []
    
    for i in range(len(s)):
        if s[i] in otw:
            stos.append(s[i])
        else:
            if len(stos) != 0:
                if s[i] == ")" and stos[-1] == "(":
                    stos.pop()
                elif s[i] == "]" and stos[-1] == "[":
                    stos.pop()
                elif s[i] == "}" and stos[-1] == "{":
                    stos.pop()
                else:
                    return False
            else:
                return False
            
    if len(stos) == 0:
        return True
    
    return False
    
def main():
    n = int(input())
    s = str(input().strip())
    
    i = 0
    max_w = -1
    akt_zag = 0
    otw = set(["{", "[", "("])
    
    if czy_poprawne(s, otw):
        while i < n:
            if s[i] in otw:
                akt_zag += 1
                max_w = max(max_w, akt_zag)
            else:
                akt_zag -= 1
                
            i += 1
    else:
        print("NIE")
        return 
    
    print(max_w)
            
main()