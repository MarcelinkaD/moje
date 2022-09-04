from sys import stdin
input = stdin.readline

def sys5(o):
	w = ""
	while o > 0:
		w = str(o % 5) + w
		o = o // 5
	return w
	
	
def main():
	n = int(input())
	liczby = [0, 2, 4, 6, 8]
	now = str(sys5(n))
	w = ""
	
	for i in now:
		w += str(liczby[int(i)])
		
	print(w)
	
	
main()
