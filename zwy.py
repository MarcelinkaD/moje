from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	zaw = list(map(int, input().split()))
	maxi = max(zaw)
	alfa = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	w = ""
	
	for i in range(n):
		if zaw[i] == maxi:
			w += alfa[i]
	
	print(w)
	
main()
