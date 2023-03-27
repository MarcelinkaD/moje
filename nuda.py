from sys import stdin
input = stdin.readline

def main():
	n, k = map(int, input().split())
	ile_zos = k
	
	if n == k:
		w = (n - 1) * "$ "
		w += "$"
		print(w)
		return 
	else:
		# ~ breakpoint()
		while ile_zos > 0:
			if n > ile_zos:
				w = (ile_zos - 1) * "$ "
				w += "$"
				ile_zos -= n
			else:
				w = (n - 1) * "$ "
				w += "$"
				ile_zos -= n
				
			print(w)
			n += 2
			
	
	
main()
