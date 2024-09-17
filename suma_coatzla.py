n = int(input())
suma = n

while n != 1:
    if n % 2 == 1:
        n = 3 * n + 1
    else:
        n //= 2
        
    suma += n
    
print(suma)