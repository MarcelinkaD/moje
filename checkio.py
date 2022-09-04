def caps_lock(text: str) -> str:
	w = text[0]
	czywl = False
	for k in range(1, len(text)):
		i = text[k]
		if i == "a" or i == "A" and k != 0:
			if czywl == False:
				czywl = True
			else:
				czywl = False
				
			continue
			
		else:
			if i.isalpha():
				if czywl == False:
					w += i
				else:
					if i.isupper() and text[k - 1] != " ":
						w += i.lower()
					else:
						w += i.upper()
			else:
				w += i
	
	return w
	


if __name__ == "__main__":
	print("Example:")
	print(caps_lock("Why are you asking me that?"))

	# These "asserts" are used for self-checking and not for an auto-testing
	assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
	assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
	assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
	print("Coding complete? Click 'Check' to earn cool rewards!")
