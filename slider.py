import math
from fractions import Fraction as f
from sys import stdin
input = stdin.readline

def main():
	n = f.from_float(int(input()))
	w = math.ceil(n / 3)
	print(w)
	
main()
