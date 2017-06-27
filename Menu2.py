no1=0
no2=0

def inputs():
	global no1
	global no2
	no1 = int (input ("Input 1st Number: "))
	no2 = int (input ("Input 2nd Number: "))

def Menu():
	print ("-----------------------")
	print ("Menu")
	print ("Please Select One Of The Following Options")
	print ("1. ADDITION")
	print ("2. SUBTRACTION")
	print ("3. DIVISION")
	print ("4. MULTIPLICATION")
	print ("5. TIMES TABLE")
	print ("6. EXIT")
	print ("-----------------------")


def add():
	inputs()
	no3 = no1 + no2
	print ("%d + %d = %d" %(no1,no2,no3))
	loop1 = True
	while loop1:
		print ("1. Try Again?")
		print ("2. Back To MainMenu")
		choice1 = int(input("Enter your choice [1-2]: "))
		if choice1 == 1:
			inputs()
		else:
			menu()
		
	
def Sub():
	inputs()
	no3 = no2 - no1
	print ("%d - %d = %d" %(no2,no1,no3))
	
def Divide():
	inputs()
	no3 = no1 / no2
	print ("%d / %d = %d" %(no1,no2,no3))

def Multiply():
	inputs()
	no3 = no1 * no2
	print ("%d X %d = %d" %(no1,no2,no3))
	
def Ttable():
	A = int (input ("Input Times Table Number: "))
	B = int (input ("Input The Range: "))
	for i in range(1,B+1):
		print(A,'x',i,'=',A*i)

	

loop=True  


while loop:
	Menu()   
	choice = int(input("Enter your choice [1-6]: "))
	
	if choice == 1:
		print("--- ADDITION ---")
		add()
		
	elif choice == 2:
		print ("--- SUBTRACTION ---")
		Sub()
	
	elif choice == 3:
		print ("--- DIVISION ---")
		Divide()
		
	elif choice == 4:
		print ("--- MULTIPLICATION")
		Multiply()
	
	elif choice == 5:
		print ("--- TIMES TABLE ---")
		Ttable()
		
	elif choice == 6:
		print ("Exit")
		
		loop=False
	else:
		input("Wrong Option Selected. Press Enter To Go Back To Main Menu.")
	input()	