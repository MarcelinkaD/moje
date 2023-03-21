import math
from decimal import Decimal as D
from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	n = D.from_float(n)
	n += n / 2
	print(math.ceil(n))
	
main()
