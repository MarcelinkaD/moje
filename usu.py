from sys import stdin
input = stdin.readline
    
def main():
	n = int(input())
	l = list(map(int, input().split()))
	wyn = 0
	
	#breakpoint()
	
	while len(l) != 0:
		
		maxi = max(l)
		pocz = l.index(maxi) 
		koniec = pocz + maxi + 1
		
		l = l[:pocz] + l[koniec:]
		wyn = wyn +1 
		
			
	print(wyn)
	
	
main()
