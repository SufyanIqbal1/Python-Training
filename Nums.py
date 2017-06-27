Ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

Tys = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

strNum = int (input ("Please Enter A Number To Convert To Words: "))

def UnderThousand(inputNum):
    num = int(inputNum)
    if (num >= 1) and (num <= 19):
        return Ones[num]
		
    elif 20 <= num <= 99:
        rem = num % 10
        dig = num / 10
        if rem == 0:
            return Tys[num]
			
        else:
            return Tys[int(inputNum[0])] + "-" + Ones[int(inputNum[1])]
			
    elif 100 <= num <= 999:
        rem = num % 100
        dig = num / 100
        if rem == 0:
            return Ones[dig] + " hundred"
        else:
            return Ones[dig] + " hundred and " + UnderThousand(str(rem))

intNum = int(strNum)
			
print (UnderThousand(strNum))