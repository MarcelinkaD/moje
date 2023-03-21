from sys import stdin
input = stdin.readline

def main():
	z_cz = str(input())
	lw, lk = map(int, input().split())
	graf = []
	for i in range(lk):
		a, b = map(int, input().split())
		graf.append([a, b])
		
	
	
main()
