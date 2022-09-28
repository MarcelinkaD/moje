from sys import stdin
input = stdin.readline

def main():
	s = str(input().strip())
	wy = 0
	w = ""
	li = []
	
	for i in range(len(s)):
		li.append(int(s[i]))
		
	for i in li:
		wy += i

	if wy % 9 == 0:
		for i in li:
			print(i, end = "")
		return 0
	else:
		ile = wy % 9
		sk = wy // 9 * 9
		sw = wy // 9 * 9 + 9
		# ~ breakpoint()
		if wy - sk > sw - wy or sk == 0:
			j = sw - wy
			for i in range(len(s)):
				if li[i] + j <= 9 and (wy + j) % 9 == 0:
					li[i] += j
					for i in li:
						print(i, end = "")
					return 0
					
			j = (wy - sk) * -1
			for i in range(len(s)):
				if (wy + j) % 9 == 0 and li[i] + j != 0:
					li[i] += j
					for i in li:
						print(i, end = "")
					return 0
			
		else:
			j = (wy - sk)
			for i in range(len(s)):
				if (wy - j) % 9 == 0 and li[i] - j >= 0:
					li[i] -= j
					for i in li:
						print(i, end = "")
					return 0
					
					
			j = sw - wy
			for i in range(len(s)):
				if li[i] + j <= 9 and (wy + j) % 9 == 0:
					li[i] += j
					for i in li:
						print(i, end = "")
					return 0
			
		
			
	

	
main()


