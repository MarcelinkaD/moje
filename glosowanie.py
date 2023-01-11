from sys import stdin
input = stdin.readline

def main():
	a, b = map(int, input().split())
	
	if a + b != 100:
		print("SKANDAL")
	elif a > b:
		print("Bitek")
	elif a < b:
		print("Bajtek")
	else:
		print("Remis")
	
main()
