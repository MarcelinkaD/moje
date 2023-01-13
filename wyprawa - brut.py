from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    l = list(map(int, input().split()))
    max_wyn = 0
    
    for i in range(n):
        w = 0
        czy_ros = True
        for k in range(i + 1, n):
            if l[k - 1] < l[k] and czy_ros:
                w += 1
            elif l[k - 1] > l[k] and czy_ros:
                w += 1
                czy_ros = False
            elif l[k - 1] > l[k] and czy_ros == False:
                w += 1
            elif l[k - 1] < l[k] and czy_ros == False:
                break
        
        max_wyn = max(max_wyn, w + 1)
        
    print(max_wyn)
    
main()

