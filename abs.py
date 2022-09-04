from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	liczby = list(map(int, input().split()))
	maxi = -11111111111
	mini = 111111111111
	
	for i in liczby:
		if i < mini:
			mini = i
		if i > maxi:
			maxi = i
	
	print(maxi - mini)
	
main()
