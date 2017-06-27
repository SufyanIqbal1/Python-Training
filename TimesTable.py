num = int (input ("Input 1st Number: "))
num2 = int (input ("Input 2nd Number: "))

while (num >= num2):
	print ("\n Times Table for: %d" %num)
	for i in range(1, 11):
		print(num,'x',i,'=',num*i)
	num = num - 1
	
while (num <= num2):
	print ("\n Times Table for: %d" %num)
	for i in range(1, 11):
		print(num,'x',i,'=',num*i)
	num = num + 1
		
