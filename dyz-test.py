from sys import stdin
input = stdin.readline
import numpy
import time

def primesVanilla(n):
    r = [True] * n
    r[0] = r[1] = False 
    r[4::2] = [False] * len(r[4::2])
    for i in range(3, int(1 + n**0.5), 2):
        if r[i]:
            r[i*i::2*i] = [False] * len(r[i*i::2*i])
    return r

def main():
	
	st = time.time()
	MAXN = int(1e6+1)
	sito = [False, True] * (MAXN//2) + [True]
	sito[1], sito[2] = False, True
		
	for i in range(3, int(MAXN**0.5+1), 2):
		if sito[i] == True:
			sito[i*i::2*i] = [False] * int((MAXN+2*i-1-i*i)/(2*i))

				
				
	#breakpoint()
	et = time.time()
	elapsed_time = et - st
	print('Execution time:', elapsed_time, 'seconds')
	
	q = int(input())
	
	for k in range(q):
		a, b = map(int, input().split())
		w = 0
		
		st = time.time()
		for i in range(a, b + 1):
			if sito[i] == True:
				w += 1
		et = time.time()
		elapsed_time = et - st
		print(' PETLA Execution time:', elapsed_time, 'seconds')
			
		print(w)

main()
