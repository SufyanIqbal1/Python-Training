with open ("ABC.txt") as f:
	newText=f.read().replace('Hello my friend', 'E')
	
with open("ABC.txt", "w") as f:
	f.write(newText)