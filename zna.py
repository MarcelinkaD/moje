from sys import stdin
input = stdin.readline
from bisect import bisect_left

def binary(li, n, pocz, kon):
	i = bisect_left(li, n, pocz, kon)
	if i != len(li) and li[i] == n:
		return i
	else:
		return -1

def main(args):
	li_zna_bi, li_zna_baj = map(int, input().split())
	zna_bi = list(map(int, input().split()))
	zna_baj = list(map(int, input().split()))
	w = 0
	ost_i = 0
	zna_baj.sort()
	zna_bi.sort()
	
	for i in zna_baj:
		z = binary(zna_bi, i, ost_i, li_zna_bi)
		if z == -1:
			w += 1
		else:
			ost_i = z
			
	print(w)




if __name__ == '__main__':
    import sys
    main(sys.argv)
