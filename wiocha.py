from sys import stdin
input = stdin.readline
    
def main():
	liczba_ziomkow, q = map(int, input().split())
	ziomki = list(map(str, input().split()))
	czy = {}
	
	for i in ziomki:
		czy[i] = (0, 0, 0)
	
	for _ in range(q):
		co_mowi = list(map(str, input().split()))
		if len(co_mowi) == 3:
			if co_mowi[2] == "orkiem.":
				czy[co_mowi[0][0:len(co_mowi[0]) - 1]][2] = 1
			elif co_mowi[2] == "krasnoludem.":
				czy[co_mowi[0][0:len(co_mowi[0]) - 1]][1] = 1
			else:
				czy[co_mowi[0][0:len(co_mowi[0]) - 1]][0] = 1
		else:
			if co_mowi[3] == "orkiem.":
				czy[co_mowi[0][0:len(co_mowi[0]) - 1]][2] = 1
			elif co_mowi[2] == "krasnoludem.":
				czy[co_mowi[0][0:len(co_mowi[0]) - 1]][1] = 1
			else:
				czy[co_mowi[0][0:len(co_mowi[0]) - 1]][0] = 1
	
	
main()
