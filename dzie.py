from itertools import accumulate
from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	wojewodztwa = map(int, input().split())
	maxi = -1
	ac = list(accumulate(wojewodztwa))
	ost = ac[len(ac) - 1]
	#breakpoint()
	for i in range(n):
		for k in range(i + 1, n):
			if (ac[k] - ac[i]) > maxi and ost - (ac[k] - ac[i]) > maxi:
					maxi = (ac[k] - ac[i]) - 1
				
	
	print(maxi)
	
main()
