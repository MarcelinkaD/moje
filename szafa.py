from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	# ~ breakpoint()
	for i in range(2, n + 1):
		dp[i] = max(l[i - 1], dp[i - 2] + l[i])
		
	print(dp[n])
	
	
main()


