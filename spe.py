from sys import stdin
input = stdin.readline
import math

def NWW(tab):
	if len(tab) > 10:
		return Error
	elif len(tab) == 2: 
		return (tab[0] // math.gcd(tab[0], tab[1]))* tab[1]
	else:
		return NWW([tab[0], NWW(tab[1 : len(tab)])])
		
def main():
	n = int(input())
	l = []
	
	for i in range(n):
		a = int(input())
		l.append(a + 1)
	
	print(NWW(l) - 1)
	
	
main()
