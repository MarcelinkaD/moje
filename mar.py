from sys import stdin
input = stdin.readline
import math

def ile_marchewek(r):
	ile = 0
	y = r
	for x in range(r + 1):
		#breakpoint()
		#print(x)
		while math.pow(x, 2) + math.pow(y, 2) > math.pow(r, 2):
			y -= 1
		ile = ile + y
	#print(ile)
	return 4 * ile + 1

def main():
	licz_mar = int(input())
	# ~ print(licz_mar)
	# ~ return 0
	l, p = 0, 20000
	# ~ breakpoint()
	while l < p:
		r = math.floor((l + p) // 2)
		ile = ile_marchewek(r)
		if ile == licz_mar:
			return r
		elif ile > licz_mar:
			p = r
		else:
			l = r + 1
			
	return p
	

print(main())

