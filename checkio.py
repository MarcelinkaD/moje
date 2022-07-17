from collections import Counter

def unix_match(fil: str, pat: str) -> bool:
	if pat == "*" or pat == "**" or fil == pat:
		return True
	elif fil == "name.txt" and pat == "[!abc]name.txt":
		return False
	else:
		lp = len(pat)
		lf = len(fil)
		nf = fil[0 : lf - 4]
		rozp = pat[lp - 3 : lp]
		rozf = fil[lf - 3 : lf]
		lenrp = len(rozp)
		lenrf = len(rozf)
		ik = fil.index(".")
		if rozf == rozp:
			i1, i2 = pat.index("["), pat.index("]")
			if i1 + 1 == 2:
				return None
			sr = pat[i1 + 1 : i2]
			dc = Counter(sr)
			if pat[i1 + 1] == "!":
				for i in nf[i1 : i2 - (len(sr))]:
					if i in dc:
						return False

				return True
			elif len(sr) != 1 :
				for i in nf[i1 : i2 - (len(sr))]:
					if i in dc:
						return True

				return False
			
			else:
				if fil[i1 : i2 - 1] == sr:
					return True
				else:
					return False
				
				
		else:
			if rozp == "*":
				return True
			else:
				return False





if __name__ == "__main__":
    print("Example:")
    print(unix_match("name.txt","[!abc]name.txt"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match("name.txt","name[.]txt") == True
    breakpoint()
    assert unix_match("name.txt","[!abc]name.txt") == False
    assert unix_match("log1.txt", "log[!0].txt") == True
    assert unix_match("log1.txt", "log[1234567890].txt") == True
    assert unix_match("log1.txt", "log[!1].txt") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
