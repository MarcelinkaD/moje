from sys import stdin
input = stdin.readline

def main():
	x1, y1 = map(str, input().split())
	x2, y2 = map(str, input().split())
	
	if x1 == x2 and y1 == y2:
		print("NIE")	
	elif x2 == x1 or y2 == y1:
		print("TAK")
	else:
		print("NIE")

main()
