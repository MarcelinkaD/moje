from sys import stdin
input = stdin.readline

def main():
	lw, lk = map(int, input().split())
	kraw = []
	for i in range(lk):
		a, b = map(int, input().split())
		kraw.append([a, b])
		
	graf = [[0 for _ in range(lw + 1)] for _ in range(lw + 1)]

	for i in kraw:
		a = i[0]
		b = i[1]
		
		graf[a][b] = 1
		graf[b][a] = 1
	
	for i in graf:
		print(i)
		
main()
