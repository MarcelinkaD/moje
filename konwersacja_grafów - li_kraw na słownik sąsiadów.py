from sys import stdin
input = stdin.readline

def main():
	lw, lk = map(int, input().split())
	kraw = []
	for i in range(lk):
		a, b = map(int, input().split())
		kraw.append([a, b])
		
	graf = {}

	for i in range(lk):
		if kraw[i][0] in graf:
			graf[kraw[i][0]].append(kraw[i][1])
		else:
			graf[kraw[i][0]] = []
			graf[kraw[i][0]].append(kraw[i][1])
		
		if kraw[i][1] in graf:
			graf[kraw[i][1]].append(kraw[i][0])
		else:
			graf[kraw[i][1]] = []
			graf[kraw[i][1]].append(kraw[i][0])
			
		
	print(graf)
	
	
main()
