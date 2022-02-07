def main():
    slowo = str(input())
    do_skreslenia = 0
    
    for i in range(1, len(slowo)):
        if(slowo[i] == slowo[i - 1]):
            do_skreslenia += 1
    
    print(do_skreslenia)
    
main()