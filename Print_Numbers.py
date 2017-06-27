Ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

Tys = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

strNum = int (input ("Please Enter A Number To Convert To Words: "))

# A recursive function to get the word equivalent for numbers under 1000.

def UnderThousand(inputNum):
    num = int(inputNum)
    if 0 <= num <= 19:
        return Ones[num]
		
    elif 20 <= num <= 99:
        if inputNum[-1] == "0":
            return Tys[int(inputNum[0])]
			
        else:
            return Tys[int(inputNum[0])] + "-" + Ones[int(inputNum[1])]
			
    elif 100 <= num <= 999:
        rem = num % 100
        dig = num / 100
        if rem == 0:
            return Ones[dig] + " hundred"
        else:
            return Ones[dig] + " hundred and " + UnderThousand(str(rem))



def Thousands(inputNum):
    num = int(inputNum)
    arrZero = splitByThousands(num)
    lenArr = len(arrZero) - 1
    resArr = []
    for z in arrZero[::-1]:
        wrd = UnderThousand(str(z)) + " "
        zap = Hunds[lenArr] + ", "
        if wrd == " ":
            break
        elif wrd == "zero ":
            wrd, zap = "", ""
        resArr.append(wrd + zap)
        lenArr -= 1
    res = "".join(resArr).strip()
    if res[-1] == ",": res = res[:-1]
    return res

# Function to return a list created from splitting a number above 1000.

def splitByThousands(inputNum):
    num = int(inputNum)
    arrThousands = []
    while num != 0:
        arrThousands.append(num % 1000)
        num /= 1000
    return arrThousands

### Last part is pretty much just the output.

intNum = int(strNum)


if intNum < 1000:
	print (UnderThousand(strNum))
else:
	print (Thousands(strNum))