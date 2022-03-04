from sys import stdin
input = stdin.readline


def isPalindrome(s):
    return s == s[::-1]

def main():
    liczba_s = int(input())
    slowa = []
    w = 0
    
    for i in range(liczba_s):
        f = str(input())
        f = f.strip()
        slowa.append(f)
        
    for i in range(len(slowa)):
        for k in range(0, len(slowa)):
             if k != i:
                 m = slowa[i] + slowa[k]
                 is_pal = isPalindrome(m)
                 
                 if is_pal:
                     w += 1
                     
    print(w)
    
main()