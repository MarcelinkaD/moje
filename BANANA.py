# źródło - https://stackoverflow.com/questions/19153462/get-excel-style-column-names-from-column-number

from sys import stdin
input = stdin.readline

def excel_style(row, col):
	LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	result = []
	while col:
		col, rem = divmod(col - 1, 26)
		result[:0] = LETTERS[rem]
	return ''.join(result) + str(row)

def main():
	q = int(input())
	
	for _ in range(q):
		n = int(input())
		w = excel_style(1, n)
		print(w[0 : len(w) - 1])
	
main()
