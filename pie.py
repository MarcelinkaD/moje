from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	pocz = 1
	kon = n
	
	while kon > pocz:
		srodek = (kon + pocz + 1) // 2
		if srodek * srodek <= n:
			pocz = srodek 
		else:
			kon = srodek - 1
			
	print(pocz)
	
main()
