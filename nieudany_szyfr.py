from sys import stdin
input = stdin.readline

def main():
	MAXN = 1000000007
	n = str(input().strip())
	dp = [0] * (len(n) + 1)
	dp[0] = 1        
	dp[1] = 1      
	
	for i in range(2, len(n) + 1):
		li = int(n[i - 2 : i])
		dp[i] = dp[i - 1]
			
		if li <= 26 and li >= 10:
			dp[i] += dp[i - 2] 
			dp[i] = dp[i] % MAXN
			
	print(dp[-1])
	
main()
