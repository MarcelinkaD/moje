from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	l.insert(0, 0)
	pref = [0] * (n + 1)
	
	for i in range(1, n + 1):
		pref[i] = l[i] + pref[i - 1]
		
	print(pref)
	
main()
