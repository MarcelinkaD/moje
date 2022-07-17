from sys import stdin
input = stdin.readline
				
def main():
	n = int(input())
	wagony = list(map(int, input().split()))
	q = int(input())
	pref = [0 for i in range(n + 1)]
	
	wagony.insert(0,0)

	for i in range(1, len(pref)):
		pref[i] = pref[i - 1] + wagony[i]
		
	for i in range(q):
		od, do = map(int, input().split())
		print(pref[do] - pref[od - 1])
	
main()
