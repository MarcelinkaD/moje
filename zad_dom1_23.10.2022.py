from sys import stdin
input = stdin.readline
    
def main():
	from collections import Counter as C
	
	n = int(input())
	l = list(map(int, input().split()))
	c = C(l)
	czy = True
	
	for i in c:
		if c[i] != 1 or i > n:
			czy = False
	if czy:
		print("TAK")
	else:
		print("NIE")
	
	
main()
