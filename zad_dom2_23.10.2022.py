from sys import stdin
input = stdin.readline
    
def main():
	n = int(input())
	l = list(map(int, input().split()))
	k = 100
	zlicz = [0 for _ in range(100 + 1)]
	
	for i in range(n):
		zlicz[l[i]] += 1
	
	l.clear()
	for i in range(k + 1):
		for j in range(zlicz[i]):
			l.append(i)
	
	print(l)
	
main()
