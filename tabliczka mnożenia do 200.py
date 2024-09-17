import random

print("ile pytań?")
n = int(input())
w = 0
print("")

for i in range(n):
    a = random.randint(10, 20)
    b = random.randint(10, 15)
    c = a * b
    print("ile to", a, "*", b)
    odpowiedz = int(input())
    
    if c != odpowiedz:
        print("źle :(")
        print("poprawna odpowiedź to", c)
    else:
        print("dobrze :D")
        w += 1
    print("")
        
print("na", n, "odpowiedzi miałaś", w, "dobrze")