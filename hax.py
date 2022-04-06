from sys import stdin
input = stdin.readline

def main():
    slowo = str(input())
    slowo_list = list(slowo)
    
    for i in range(len(slowo)):
        if slowo_list[i] == "a":
            slowo_list[i] = "4"
        elif slowo_list[i] == "e":
            slowo_list[i] = "3"
        elif slowo_list[i] == "i":
            slowo_list[i] = "1"
        elif slowo_list[i] == "o":
            slowo_list[i] = "0"
        elif slowo_list[i] == "s":
            slowo_list[i] = "5"
            
    print("".join(slowo_list))
    
main()