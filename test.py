start = int (input ("Input 1st Number: "))
end = int (input ("Input 2nd Number: "))

step = 1

if start > end:
	step = - 1
	end  = - 1
	
	print("%d %d %d" %(start,end,step))
for T in range(start,end + 1,step):
	for B in range(1,11):
		print(" %d x %d =%d" %(T,B,(T*B)))