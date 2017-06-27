try:
	A = int (input ("Input Times Table Number: "))
	B = int (input ("Input The Range: "))
	for i in range(1,B+1):
		print(A,'x',i,'=',A*i)
except:
	print ("Boy put in a number")