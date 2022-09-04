from sys import stdin
input = stdin.readline

def main():
	d, k = map(int, input().strip().split())
	latarnie = []
	for i in range(k):
		l = int(input().strip())
		latarnie.append(l)

#	print(latarnie.replace(" ", "__")+"_____"+latarnie2.replace(" ", "__"))
	
	latarnie.sort()
	maxi = 0
	
	if k == 1:
		print(float(latarnie[0]))
		return 
		
	

	for i in range(k - 1):
		pie = latarnie[i]                 
		dru = latarnie[i + 1]
		odl = dru - pie
		if odl > maxi:
			maxi = odl
	
	maxi = maxi / 2
			
	if d - latarnie[k - 1] > maxi:
		print(float(d - latarnie[k - 1]))
		return
	elif latarnie[0] - 0 > maxi:
		print(float(latarnie[0] - 0))
		return
	
	print(float(maxi))
	return
	
main()

