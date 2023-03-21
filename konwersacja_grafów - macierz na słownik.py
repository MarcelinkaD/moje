from sys import stdin
input = stdin.readline

def main():
	lw, lk = map(int, input().split())
	mac = []
	
	for _ in range(lw):
		l = list(map(int, input().split()))
		mac.append(l)
		
	graf = {}
	
	for a in range(lw):
		for b in range(lw):
			if mac[a][b] == 1:
				if a in graf:
					graf[a].append(b)
				else:
					graf[a] = []
					graf[a].append(b)
					
					
	print(graf)
	
main()
