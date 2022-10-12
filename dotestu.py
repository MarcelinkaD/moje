from sys import stdin
input = stdin.readline

def f(a, b):
	if b == 0: return 0
	h = f(a, b // 2) * 2
	if b % 2 == 0: return h
	return h + a

def main():
	# ~ breakpoint()
	print(ord("a"))
	
	
main()
