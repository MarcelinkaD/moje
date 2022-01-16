n = int(input())
pomiary = list(map(int, input().split()))
poprzedniPomiar = pomiary[0]
baseny = 1
rosnie = True

for  i in pomiary:
    if (rosnie == True) and (i < poprzedniPomiar):
        baseny += 1
        rosnie = False
    elif(rosnie == False) and (i > poprzedniPomiar):
        baseny += 1
        rosnie = True
    poprzedniPomiar = i

print(baseny)