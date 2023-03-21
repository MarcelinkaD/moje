from sys import stdin
input = stdin.readline

def main():
	sz, spanie, pryw = map(int, input().split())
	ile_zos = 24 - pryw
	
	print((sz + spanie) - ile_zos)
	
main()

