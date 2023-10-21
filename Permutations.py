# https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/795/

def gen(akt_w, w, l):
    if len(l) != 1:
        for k in range(len(l)):
            gen(akt_w + [l[k]], w, l[0 : k] + l[k + 1 : len(l)])
    else:
        w.append(akt_w + [l[0]])

def permute(l):
    w = []
    
    if len(l) == 1:
        return [[l[0]]]
    
    for i in range(len(l)):
        gen([l[i]], w, l[0 : i] + l[i + 1 : len(l)])
    
    return w

print(permute([1]))