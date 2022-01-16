import math

n = int(input())
dzielniki = []



for i in range(1, int(math.sqrt(n))+1):
    if(n % i == 0):
        dzielniki.append(i)
        drugiDzielnik = n/i

        if(drugiDzielnik != i):      
            dzielniki.append(int(drugiDzielnik))

dzielniki.sort()

for i in dzielniki:
    print(i)

