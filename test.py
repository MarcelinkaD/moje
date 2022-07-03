from sys import stdin
input = stdin.readline

def binary(li, n):
	kon = len(li)
	pocz = 0
	while pocz < kon:
		sro = (pocz + kon) // 2
		if li[sro] < n:
			pocz = sro + 1
		else:
			kon = sro
			
	return pocz
