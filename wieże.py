from collections import Counter as C
from sys import stdin
input = stdin.readline

def czy_pust(l, i):
	for k in range(len(l)):
		if l[k][i] == "W":
			return False
			
	return True

def main():
	n = int(input())
	plansza = []
	ilew = 0
	jakie_wiersze_puste = []
	
	for k in range(n):
		i = str(input().strip())
		c = C(i)
		if "W" in c:
			ilew += c["W"]
		else:
			jakie_wiersze_puste.append(k) 
			
		plansza.append(i)
			
	iledopos = n - ilew
	jakie_kolumny_puste = []
	for i in range(n):
		if czy_pust(plansza, i):
			jakie_kolumny_puste.append(i)
		
	w = []
	
	for i in range(n):
		# ~ breakpoint()
		if i not in jakie_wiersze_puste:
			w.append(plansza[i])
		else:
			cododod = ""
			for k in range(n):
				if k in jakie_kolumny_puste:
					cododod += "W"
					jakie_kolumny_puste.remove(k)
					break
				else:
					cododod += "."
					
			cododod += "." * (n - len(cododod))
			
			w.append(cododod)
	
	for i in w:
		print(i)
		
	
	
	
	
main()


