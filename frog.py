from sys import stdin
input = stdin.readline

def main():
    len_tab = int(input())
    kamienie = list(map(int, input().split()))
    dy = [0] * (len_tab + 1)
    kamienie.insert(0, 100500100900)
    
    for i in range(2, len_tab + 1):
        dy[i] = min(dy[i - 1] + abs(kamienie[i - 1] - kamienie[i]), dy[i - 2] + abs(kamienie[i - 2] - kamienie[i]))
        
    print(dy[len_tab])
    
main()