def binary(pocz, kon):
	while pocz < kon:
		srodek = (pocz + kon) // 2
		if f(srodek) == True:
			pocz = srodek
		else:
			kon = srodek - 1
	
	return pocz
