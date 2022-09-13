from collections import Counter as C
import bisect as bi
from sys import stdin
input = stdin.readline

def czy_moge(n, b, pop, licz):
	s = 0
	g = 0
	while b <= n:
		b += pop
		g += 1
		s += 1
		licz -= 1
		
		if licz <= 0:
			print("NIE")
			return 0
	
	return (g * n, s)

def main():
	n = int(input())
	kom = list(map(int, input().split()))
	kom.sort()
	baj = 2
	sek = 0
	c = C(kom)
	pop = 0
	i = 1
	maxi = kom[len(kom) - 1]
	breakpoint()
	while i < maxi - 1:
		if i == 1:
			if baj > kom[0]:
				baj += kom[0]
				sek += 1
			else:
				print("NIE")
				return 0
			pop = kom[0]
		else:
			k = bi.bisect_left(kom, i)
			if kom[k] < baj:
				baj += kom[i]
				sek += 1
				pop = kom[i]
			else:
				c = czy_moge(kom[k], baj, pop, C[pop])
				baj += c[0]
				sek += c[1]
				
		if baj >= maxi:
			print(sek)
			return 0
			
		i += 1
		
	if baj >= maxi:
		print(sek)
		return 0
	else:
		print("NIE")
		return 0
	
	
	
main()
