from sys import stdin
input = stdin.readline

def main():
	k2, k3, k5, k6 = map(int, input().split())
	w256 = 0
	w32 = 0
	w = 0

	if k2 < k6 and k2 < k5 and k2 != 0:
		w += 256 * k2
		k2 = 0
	elif k6 < k2 and k6 < k5 and k6 != 0:
		w += 256 * k6
		k2 -= k6
	elif k5 < k2 and k5 < k6 and k5 != 0:
		w += 256 * k5
		k2 -= k5
	elif k5 != 0 and k6 != 0 and k2 != 0:
		w += 256 * k5
		k2 = 0
		
	if k2 < k3:
		w += 32 * k2
	elif k2 != 0:
		w += 32 * k3
	
		
	# ~ while k2 != 0 and k5 != 0 and k6 != 0:
		# ~ k2 -= 1
		# ~ k5 -= 1
		# ~ k6 -= 1
		# ~ w256 += 256
	
	# ~ while k2 != 0 and k3 != 0:
		# ~ k2 -= 1
		# ~ k3 -= 1
		# ~ w32 += 32
		
	# ~ w += w32 + w256
	
	return w
	
print(main())
