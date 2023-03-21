# https://szkopul.edu.pl/c/testowy_dd/p/gru/18867/

from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	wg, wj = 0, 0
	wg2, wj2 = 0, 0
	git1 = False
	git2 = False
	git3 = False
	git4 = False
	
	for i in range(n):
		if git1 == False and l[i] == 0:
			wg = i
			git1 = True
		
		if git2 == False and l[i] == 1:
			wj2 = i
			git2 = True
			
		if git1 and git2:
			break

	for i in range(n - 1, -1, -1):
		if git3 == False and l[i] == 1:
			wj = i
			git3 = True
		
		if git4 == False and l[i] == 0:
			wg2 = i
			git4 = True
			
		if git4 and git3:
			break
		
	
	w1 = wj - wg
	w2 = wg2 - wj2
	w3 = wg2 - wj
	w4 = wj2 - wg
	
	print(max(max(w1, w2), max(w3, w4)))
	
	
main()

