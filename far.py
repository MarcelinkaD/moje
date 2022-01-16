lg , ln = map(int, input().split())

ilePelnychRozdan = 0

while(ln >= 2*lg):
    ilePelnychRozdan += 1
    ln -= lg * 2 

if(ilePelnychRozdan == 1):
    krowy = ln / 2
else:
    krowy = lg


kury = lg - krowy

print(str(int(kury)) + " " + str(int(krowy)))
