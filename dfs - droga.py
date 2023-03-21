droga = []

def dfs(w, droga, graf):
	droga.append(w)
	odw[w] = True
	print(droga)
	for sasiad in graf[w]:
		if not odw[sasiad]:
			dfs(sasiad, droga, graf)
			
	droga.remove(w) # nie wiem czy zadziała 
    
dfs(1, droga, graf)
