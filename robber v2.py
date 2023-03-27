from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	l.insert(0, 0)
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = max(l[1], l[2] + l[n])

	for i in range(2, n):
		dp[i] = max(l[i + 1] + l[i - 1], dp[i - 1])
		
	dp[n] = max(l[2] + l[n], dp[n - 1])
	
	print(dp[n])
	
main()
