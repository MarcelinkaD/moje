from sys import stdin
input = stdin.readline

def main():
	lw, lk = map(int, input().split())
	graf = [[] for _ in range(lw + 1)]
	
	for _ in range(lk):
		w1, w2 = map(int, input().split())
		graf[w1].append(w2)
		graf[w2].append(w1)
		
	q = int(input())
	
	for _ in range(q):
		w1, w2 = map(int, input().split())
		
		if w2 in graf[w1]:
			print("YES")
		else:
			print("SORRY...")
			
	
		
main()
