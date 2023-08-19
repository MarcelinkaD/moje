# https://py.checkio.org/pl/mission/the-longest-palindromic/

def czy_pal(s):
    return s == s[::-1]

def longest_palindromic(a):
    max_w = -1
    ost_w = ""
    
    for i in range(len(a)):
        for k in range(i, len(a)):
            if czy_pal(a[i:k + 1]):
                if len(a[i:k + 1]) > max_w:
                    max_w = len(a[i:k + 1])
                    ost_w = a[i:k + 1]
                    
    return ost_w
            

print("Example:")
print(longest_palindromic("abc"))

# These "asserts" are used for self-checking
assert longest_palindromic("abc") == "a"
assert longest_palindromic("abacada") == "aba"
assert longest_palindromic("artrartrt") == "rtrartr"
assert longest_palindromic("aaaaa") == "aaaaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")

