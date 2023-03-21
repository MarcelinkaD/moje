from sys import stdin
input = stdin.readline

def DFS(w, droga, graf, odw):
	odw[w] = True
	stos = [w]
	
	droga = [w]
	
	while len(stos) != 0:
		u = stos.pop()
		
		for sasiad in graf[u]:
			if not odw[sasiad]:
				stos.append(sasiad)
				droga.append(sasiad)
				print(droga)
				
		odw[u] = True
		
	
	
def main():
	n, k = map(int, input().split())
	graf = [[] for _ in range(n + 1)]
	odw = [False] * len(graf)
	
	for _ in range(k):
		a, b = map(int, input().split())
		graf[a].append(b)
		graf[b].append(a)
		
	DFS(1, [], graf, odw)
	
main()
