from fractions import Fraction
from sys import stdin
input = stdin.readline

def main():
	a, b, c, d = map(int, input().split())
	u1 = Fraction(a, b)
	u2 = Fraction(c, d)
	w = u1 + u2
	
	return str(w.numerator) + "/" + str(w.denominator)
		
print(main())
