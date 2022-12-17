from sys import stdin
input = stdin.readline

def binary(li, n):
	pocz = 0
	kon = len(li)
	while pocz < kon:
		srodek = (pocz + kon) // 2
		if li[srodek] < n:
			pocz = srodek + 1
		elif li[srodek] > n:
			kon = srodek
		else:
			return "TAK"
			
			
	return "NIE"

def main():
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	l.sort()
	# ~ breakpoint()
	print(binary(l, k))
	
main()

