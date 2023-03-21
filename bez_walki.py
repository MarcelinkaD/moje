from sys import stdin
input = stdin.readline

def main():
	n = int(input())
	l = list(map(int, input().split()))
	mini = int(1e6 + 5)
	w = 0
	for i in range(1, n):
		if l[i - 1] < mini and l[i - 1] != 0:
			mini = l[i - 1]
		w = max(l[i] - mini, w)
		
	if w <= 0:
		print("Nie ma zysku, to ci sie nie oplaca")
	else:
		print(w)
	
	
main()
