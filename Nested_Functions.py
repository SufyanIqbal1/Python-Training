

def choice (A):
	if A == 1:
		def X (A,B):
			print (" %d + %d = %d" %(A,B,(A+B)))
	else:
		def X (A,B):
			print (" %d - %d = %d" %(A,B,(A-B)))
	return X
	

F = choice (2)
F(2,3)