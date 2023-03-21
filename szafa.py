from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	l.insert(0, 0)
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = l[1]

	for i in range(2, n + 1):
		dp[i] = max(l[i] + dp[i - 2], dp[i - 1])
	
	print(dp[n])
	
	
main()


