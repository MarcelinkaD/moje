# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793/
    
def f(akt_w, akt_n, litery, n, akt_ind, w):
    if akt_ind < len(n) - 1:
        for i in litery[akt_n]:
            f(akt_w + i, n[akt_ind + 1], litery, n, akt_ind + 1, w)
    else:
        for i in litery[akt_n]:
            w.append(akt_w + i)
    
def letterCombinations(n):
    w = []
    litery = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
    
    if len(n) == 0:
        return []
    
    if len(n) == 1:
        for j in litery[n[0]]:
            w.append(j)
        return w
    
    for k in litery[n[0]]:
        f(k, n[1], litery, n, 1, w)
    
    return w
    
print(letterCombinations("999"))
    
    
        