

class ONS:
	def Message (self):
		print ("Hello")
		self.add (7,2)
		
	def add (self, A, B):
		C = A + B
		print ("Result: %d" %C)
		self.add1(2,4,5,6,7,8,9)
	
	def add1 (self, *A):
		C = 0
		for T in A:
			C = C + T
		print ("Result: %d" %C)
		self.add2(2,4,9)

	def add2 (self, A=0, B=0, C=0):
		D = A + B + C
		print ("Result: %d" %D)		
	


	
Ref = ONS()
Ref.Message()
