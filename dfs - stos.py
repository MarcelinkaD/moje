from sys import stdin
input = stdin.readline

def DFS(w, graf):
	odw = [False] * len(graf)
	odw[w] = True
	stos = [w]
	
	while len(stos) != 0:
		u = stos.pop()
		for sasiad in graf[u]:
			if not odw[sasiad]:
				stos.append(sasiad)
				
		odw[u] = True
		
	return odw

def main():
	n, k = map(int, input().split())
	graf = [[] for _ in range(n + 1)]
	
	for _ in range(k):
		a, b = map(int, input().split())
		graf[a].append(b)
		graf[b].append(a)
		
	print(DFS(1, graf))
	
	
main()
