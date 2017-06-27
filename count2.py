string2 = input ("Input Your Sentence: ")


def count_char(string1):
	lst=[]
	lst1=[]
	for i in string1:
		count=0
		if i not in lst:
			for j in string1:
				if i==j:
					count+=1
			lst1.append(i)
			lst1.append(count)
		lst.append(i)

	string2=''.join(str(x) for x in lst1)
	return (string2) 
	print (count)