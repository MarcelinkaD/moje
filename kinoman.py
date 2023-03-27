# https://szkopul.edu.pl/c/zlo155/p/kin/

from sys import stdin
input = stdin.readline

def order(x):
	return (x[1], x[0])

def main():
	n = int(input())
	odc = []
	
	for _ in range(n):
		od, do = map(int, input().split())
		odc.append([od, do])
		
	odc = sorted(odc, key = lambda j: order(j))
	w = 1
	ost_kon = odc[0][1]
	# ~ breakpoint()
	for i in range(n):
		if ost_kon < odc[i][0]:
			w += 1
			ost_kon = odc[i][1]
			
	print(w)
	
	
main()
