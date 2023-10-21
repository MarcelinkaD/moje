# https://leetcode.com/problems/valid-parentheses/

def isValid(s):
    c = {}
    
    for i in s:
        if i == "(" or i == "{" or i == "[":
            if i not in c:
                c[i] = 0
            c[i] += 1
        else:
            czy_ma = False
            for k in c:
                if k == "(" and i == ")":
                    c[k] -= 1
                    czy_ma = True
                elif k == "{" and i == "}":
                    c[k] -= 1
                    czy_ma = True
                elif k == "[" and i == "]":
                    c[k] -= 1
                    czy_ma = True
            
            if not czy_ma:
                return False
            
    
    for i in c:
        if c[i] != 0:
            return False
    
    return True

print(isValid("()[]{}"))