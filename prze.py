from sys import stdin
input = stdin.readline
				
def main():
	q = int(input())
	
	for k in range(q):
		a, b = map(str, input().split())
		l = []
		la, lb = len(a), len(b)
		w = 0
		
		liczba_wieksza = ""
		liczba_mniejsza = ""
				
		if lb < la:
			liczba_wieksza = a
			liczba_mniejsza = b
			la = len(liczba_wieksza)
			lb = len(liczba_mniejsza)
		elif lb > la:
			liczba_wieksza = b
			liczba_mniejsza = a
			la = len(liczba_wieksza)
			lb = len(liczba_mniejsza)

		else:
			liczba_wieksza = a
			liczba_mniejsza = b
			la = len(liczba_wieksza)
			lb = len(liczba_mniejsza)
			

		for i in range(la - 1, -1, -1):
			l.append(int(liczba_wieksza[i]))
		
		if lb == 1:
			l[0] += int(liczba_mniejsza)
		else:
			liczba_mniejsza = liczba_mniejsza[::-1]
			for i in range(lb):
				l[i] += int(liczba_mniejsza[i])
		
		
		for i in range(len(l)):
			if i != len(l) - 1:
				if l[i] >= 10:
					l[i] -= 10
					l[i + 1] += 1
					w += 1
			else:
				if l[i] >= 10:
					w += 1
				print(w)		

				
				
		
			
			
				
		

main()
