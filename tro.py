boki = list(map(int, input().split()))


boki.sort()


if(boki[0] + boki[1] > boki[2]):
    print("TAK")
else:
    print("NIE")