from collections import Counter as C
from sys import stdin
input = stdin.readline

def main():
	s1, s2 = map(str, input().split())
	c1, c2 = C(s1), C(s2)
	if c1 == c2:
		print("tak")
	else:
		print("nie")
		
	
main()
