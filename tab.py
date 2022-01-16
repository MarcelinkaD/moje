a, b = map(int, input().split())


if((a*b)%2==0):
    print(0)
else:
    if(a < b):
        print(a)
    else:
        print(b)