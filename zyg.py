from fractions import Fraction as F
import math
from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	ruchy = str(input().strip())
	
	s_x, s_y = 0,0
	for znak in ruchy:
		if znak == "G" : s_y += 1
		elif znak == "P" : s_x += 1
	
	
	x, y  = s_x, s_y
	ulamek = s_y / s_x
	p, q = 0, 0
	zygzak = ""
	#breakpoint()
	while p < x or q < s_y:
		
		if s_x*(q + 1) <= (s_y * p ):
			q += 1
			zygzak += "G"
		else:
			p += 1
			zygzak += "P"
	
	

	if zygzak == ruchy:
		przez = math.gcd(s_x, s_y)
		x = s_x // przez
		y = s_y // przez
		print(str(y) + "/" + str(x))
	else:
		print("NIE")
	
main()




