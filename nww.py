from decimal import Decimal as D
from sys import stdin
input = stdin.readline

def NWD(n, k):
	reszta = 0
	while k > 0:
		reszta = n % k
		n, k = k, reszta
		
	return n
    
def NWW(l, a):
	# ~ l = D.from_float(l)
	# ~ a = D.from_float(a)
	return (l * a) // NWD(l, a)
    
def main():
	c, b = map(int, input().split())
	print(int(NWW(c, b)))

main()
