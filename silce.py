from sys import stdin
input = stdin.readline
    
def solution(m, l):
	n = len(l)
	glowa = -1
	wyn = 0
	ogon = 0
	is_in_set = [0 for _ in range(m)]
	
	while glowa < n - 1:
		glowa += 1
		while is_in_set[l[glowa]] == 1:
			is_in_set[l[ogon]] = 0
			ogon += 1
		
		is_in_set[l[glowa]] = 1
		wyn += (glowa - ogon + 1)
				
	if wyn > 1e9:
		return 1e9
	return wyn 
	
main()
