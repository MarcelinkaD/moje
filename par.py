from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = []
	w = [[0, 0] for i in range(n)]
	
	for _ in range(n):
		l.append(int(input()))
		
	na_zachod = l[0]
	# ~ breakpoint()
	for i in range(n):
		if l[i] > na_zachod:
			w[i][0] = l[i]
			na_zachod = l[i]
		else:
			w[i][0] = na_zachod
			
	na_wschod = l[n - 1]
	for i in range(n - 1, -1, -1):
		if l[i] > na_wschod:
			w[i][1] = l[i]
			na_wschod = l[i]
		else:
			w[i][1] = na_wschod
			
	for i in w:
		print(i[0], end = " ")
		print(i[1]) 
	
main()
