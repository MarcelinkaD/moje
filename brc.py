from sys import stdin
input = stdin.readline

def main():
	st = str(input())
	s = 0

	for i in st:
		if i.isdigit():
			s += int(i)
			
	mod = s % 9
	return 9 - mod
	
	
print(main())
