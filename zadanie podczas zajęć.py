from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	
	if l[n - 1] == 0:
		print("0")
		
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = 1
	
	for i in range(k, n + 1):
		if l[i - 1] == 0:
			dp[i] = 0
		else:
			dp[i] = dp[i - 1] + dp[i - 2]
		
	print(dp[n])
	
main()

