from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	l.insert(0, 0)
	dp = [0] * (n + 1)
	dp[0] = 0
	dp[1] = l[1]
	
	for i in range(2, n):
		dp[i] = max(l[i] + dp[i - 2], dp[i - 1])
		
	w1 = dp[n - 1]
	
	dp = [0] * (n + 1)
	
	dp[2] = l[2]
	
	for i in range(3, n + 1):
		dp[i] = max(l[i] + dp[i - 2], dp[i - 1])
	
	w2 = dp[n]
	
	print(max(w1, w2))
	
main()
