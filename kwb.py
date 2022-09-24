from sys import stdin
input = stdin.readline

def main():
	lwie, lkol = map(int, input().split())
	li = []
	w = -1
	l = 0
	
	for i in range(lwie):
		wiersz = list(map(int, input().split()))
		li.append(wiersz)
	
	for i in range(lwie):
		for k in range(lkol):
			# ~ breakpoint()
			war = li[i][k]
			if war != 0:
				if w == -1:
					w = war
					l = 1
				else:
					if war != w:
						l -= 1
						if l == 0:
							w = -1
					else:
						l += 1
						
	print(w)
	
	
	
main()

