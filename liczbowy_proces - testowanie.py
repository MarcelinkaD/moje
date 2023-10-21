def f(x):
    w = 0
    x = str(x)
    
    for i in x:
        w += int(i)
        
    return w

def g(x):
    return x + (f(x) ** 2)

q = 500
l = 0
x = 1
while l < q:
    print(x)
    x = g(x)
    l += 1
    