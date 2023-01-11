import math
from sys import stdin
input = stdin.readline
        
def main():
	c = str(input()).strip()
	k = int(input())
	ciag = [] 

	for i in c:
		ciag.append(i)
		
	ciag.sort()
	przyszle = [""]  *  k
	kto_teraz = 0

	while len(ciag) != 0:
		if len(przyszle[kto_teraz]) == 0:
			for i in ciag:
				if i != "0":
					przyszle[kto_teraz] += i
					break
					
			ciag.remove(i)
		else:
			przyszle[kto_teraz] += ciag[0]
			ciag.remove(ciag[0])
		
		kto_teraz += 1
		
		if kto_teraz == len(przyszle):
			kto_teraz -= len(przyszle)
			
	w = 0
	
	for i in przyszle:
		w += int(i)
		
	print(w)
			
   
    
main()
