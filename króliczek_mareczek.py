from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	mar = list(map(int, input().split()))
	mar.insert(0, 0)
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = mar[1]
	
	for i in range(2, n + 1):
		dp[i] = max(mar[i] + dp[i - 2], dp[i - 1])
		
	print(dp[n])
	
main()
