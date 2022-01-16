word = str(input())
duze = 0
male = 0


for literka in word:
    if(literka.isupper()):
        duze += 1
    if(literka.islower()):
        male += 1
    
if(duze > male):
    print(word.upper())
else:
    print(word.lower())