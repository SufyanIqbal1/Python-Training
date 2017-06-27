Salary = input ("Please Insert Salary Amount: ")
Grade = input ("Please Insert Grade: ")
Department = input ("Please Insert Department - (1 = IT / 2 = HR) : ")
CTO = input ("Are You A CTO? - (1 = Yes / 2 = No) : ")

Salary = int (Salary)
Grade = int (Grade)
Department = int (Department)
CTO = int (CTO)
Bonus=0
Tax=0

if Salary > 15000:
	if (Department == 1):
		if (CTO == 1):
			SalaryAfterTax=Salary
		elif(Grade >=1 and Grade <=10):
			Tax = Salary * 0.09			
		elif (Grade >=11 and Grade <=20):
			Tax = Salary * 0.15			
		CalcBonus = SalaryAfterTax * 0.05
		Bonus = CalcBonus + SalaryAfterTax
	
	else:
		if (CTO == 1):
			Tax = Salary * 0.02				
		elif(Grade >=1 and Grade <=10):
			Tax = Salary * 0.09							
		elif (Grade >=11 and Grade <=20):
			Tax = Salary * 0.17
			
SalaryAfterTax = Salary - Tax
print ( "Salary:%d" % Salary)
print (" Tax:%f" % Tax)
print (" Salary After Tax - : %d" %(SalaryAfterTax))
print (" Salary With Added Bonus: %d" %(Bonus))		