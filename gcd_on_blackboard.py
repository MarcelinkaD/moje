from sys import stdin
input = stdin.readline

def main():
	import math
	n = int(input())
	l = list(map(int, input().split()))
	prefiksy = [0] * n
	sufixy = [0] * n
	prefiksy[0] = l[0]
	sufixy[n - 1] = l[n - 1]
	
	for i in range(1, n):
		prefiksy[i] = math.gcd(prefiksy[i - 1], l[i])
		
	for i in range(n - 2, -1, -1):
		sufixy[i] = math.gcd(sufixy[i + 1], l[i])
		
	w = max(prefiksy[n - 2], sufixy[1])
	for i in range(n - 2):
		w = max(w, math.gcd(prefiksy[i], sufixy[i + 2]))
	
	print(w)
	
main()
