#https://stackoverflow.com/questions/70635382/fastest-way-to-produce-a-list-of-all-divisors-of-a-number - z tąd pomysł

import math
from sys import stdin
input = stdin.readline

def getDivs(N):
	factors = {1}
	maxP  = int(N**0.5)
	p,inc = 2,1
	
	while p <= maxP:
		while N%p==0:
			factors.update([f*p for f in factors])
			N //= p
			maxP = int(N**0.5)
		p,inc = p+inc,2
	if N>1:
		factors.update([f*N for f in factors])
	return sorted(factors)  


def main():
	q = int(input())
	
	for _  in range(q):
		pole = int(input())
		naj_w = 1e8
		dzielniki = getDivs(pole)
		ran = len(dzielniki) // 2
		
		if pole == 1:
			print(8)
			continue
		else:
			for i in range(ran, 0, -1):
					d1 = dzielniki[i]
					d2 = pole // d1
					if d1 * d2 == pole:
						w = (d1 * 2) + (d2 * 2) + 4
						naj_w = min(w, naj_w)
						break
		
		print(int(naj_w))
	
main()
