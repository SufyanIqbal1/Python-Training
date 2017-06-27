class Results:

	def __init__ (self, P=0, C=0, M=0):
		self.__Phy = P
		self.__Che = C
		self.__Mat = M
		self.__ModulesFailed = 0
	
	def Physics (self, P):
		if (P >= 0 and P <= 150):
			self.__Phy = P
			
			if (P < 70):
				print ("Failed Physics")
				self.__ModulesFailed += 1			
	
		else:
			print ("Invalid Physics Marks")
			
	def Chemistry (self, C):
		if (C >= 0 and C <= 150):
			self.__Che = C
			
			if (C < 70):
				print ("Failed Chemistry")
				self.__ModulesFailed += 1			
		
		else:
			print ("Invalid Chemistry Marks")
			
	def Maths (self, M):
		if (M >= 0 and M <= 150):
			self.__Mat = M
			
			if (M < 70):
				print ("Failed Physics")
				self.__ModulesFailed += 1
	
		else:
			print ("Invalid Maths Marks")
			
		
	def Calculations (self):
		self.Total = self.__Phy + self.__Che + self.__Mat
		self.Percent = self.Total * (100/450)
		
	def ShowResults (self):
		print (self.Total)
		print (self.Percent)
		
		if (self.__ModulesFailed == 1):
			print ("Retake The Exam")

		elif (self.__ModulesFailed == 2):
			print ("Repeat The Course")
		
		elif (self.__ModulesFailed == 3):
			print ("Go Home")
		
		
Peter = Results(0,0,0)
Peter.Physics(1)
Peter.Chemistry(10)
Peter.Maths(2)
Peter.Calculations()
Peter.ShowResults()