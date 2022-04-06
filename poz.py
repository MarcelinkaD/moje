from sys import stdin
input = stdin.readline

def main():
    ile_razy = int(input())
    pasma = [" @@@   @@@ ", "@   @ @   @", "@    @    @", "@         @", " @       @ ", "  @     @  ", "   @   @   ", "    @ @    ", "     @     "]
        
    for k in pasma:
        w = ""
        for i in range(ile_razy):
            w += k + " "
            
        print(w)
    
main()