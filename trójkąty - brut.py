from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	w = 0
	
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j + 1 , n):
				if l[i] + l[j] > l[k] and  l[k] + l[j] > l[i] and l[i] + l[k] > l[j]:
					w += 1
					
	print(w)
	
main()
