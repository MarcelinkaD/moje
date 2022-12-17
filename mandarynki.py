from sys import stdin
input = stdin.readline
import math

def NWW(a, b):
	return a * (b / math.gcd(a, b))


def main():
	x = int(input())
	najleprze_nww = -1
	najleprzy_nwd = -1
	
	for i in range(1, x + 1):
		for k in range(i + 1, x + 1):
			gcd = math.gcd(i, k)
			nww = NWW(i, k)
			if gcd > najleprzy_nwd:
				najleprzy_nwd = gcd
			if nww > najleprze_nww:
				najleprze_nww = nww
				
	print(int(najleprze_nww + najleprzy_nwd))
	
main()
 
