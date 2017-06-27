class ONE:
	def __init__ (self, a=0, b=0, c=0):
		self.A = a
		self.B = b
		self.C = c
	
	def __add__ (self, R):
		C = ONE (0,0,0)
		C.A = self.A + R.A
		C.B = self.B + R.B
		C.C = self.C + R.C
		return C
		
	def __mul__ (self, R):
		C = ONE (0,0,0)
		C.A = self.A * R.A
		C.B = self.B * R.B
		C.C = self.C * R.C
		return C
		
	def __sub__ (self, R):
		C = ONE (0,0,0)
		C.A = self.A - R.A
		C.B = self.B - R.B
		C.C = self.C - R.C
		return C
		
	def __truediv__ (self, R):
		C = ONE (0,0,0)
		C.A = self.A / R.A
		C.B = self.B / R.B
		C.C = self.C / R.C
		return C
		
A = ONE(1,2,3)
B = ONE(10,20,30)

C = A + B

X = A * B

Y = A - B

Z = A / B

print ("Addition")
print (C.A)
print (C.B)
print (C.C)

print ("Multiplication")
print (X.A)
print (X.B)
print (X.C)

print ("Subtraction")
print (Y.A)
print (Y.B)
print (Y.C)

print ("Division")
print (Z.A)
print (Z.B)
print (Z.C)