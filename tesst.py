def reverse(s):
    j = ""
    for i in range(len(s) - 1, -1, -1):
        j += s[i]
    
    return j

bh = str(input())
print(reverse(bh))
