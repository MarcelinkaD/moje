from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	dp_o = [0] * (n + 1) 
	dp_m = [0] * (n + 1)
	dp_m[0] = 1
	
	for i in range(1, n + 1):
		dp_o[i] = dp_m[i - 1]
		dp_m[i] = (dp_o[i - 1] + dp_m[i - 1]) % 1000000007
		
	print(dp_o[n])
	
	
	
main()
