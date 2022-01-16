kon = int(input())

wszystkiekoncerty = list(map(int, input().split()))

sumypref = [0] * (kon +1 )

for i in range(kon):
    sumypref[i] = wszystkiekoncerty[i] + sumypref[i - 1]


ilepytan = int(input())

for i in range(ilepytan):
    od, do = map(int, input().split())
    print(sumypref[do - 1] - sumypref[od - 1 - 1])