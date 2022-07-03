def is_acceptable_password(s):
	breakpoint()
	p = "password"
	c = "p"
	l = 0
	for i in s:
		if i == c and l == len(p):
			return False
		elif i == c:
			l += 1
			c = p[l]
			
	if len(s) >= 9:
		return True
	elif s.isdigit():
		return False
   
        
	else:
		if len(s) <= 6:
			return False
		else:
			if s[len(s) - 1].isdigit() == True:
				return True
			else:
				return False

if __name__ == "__main__":
    assert is_acceptable_password("password12345") == False
    assert is_acceptable_password("PASSWORD12345") == False
    assert is_acceptable_password("pass1234word") == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
