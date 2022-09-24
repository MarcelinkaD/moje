class Solution:
	def leaders(self, a, n):
		w = []
		maxi = 0
		for i in range(n - 1, -1, -1):
				if a[i] >= maxi:
					maxi = a[i]
					w.append(maxi)
		# ~ breakpoint()
		w.reverse()
		return w


	import math

def main():
	
	T=int(input())
	
	while(T>0):
		
		
		N = int(input())
		
		A=[int(x) for x in input().strip().split()]
		obj = Solution()
		A=obj.leaders(A,N)
		
		for i in A:
			print(i,end=" ")
		print()
		
		T-=1
		
		
		
		
		
		
		
		
if __name__ == "__main__":
	main()
