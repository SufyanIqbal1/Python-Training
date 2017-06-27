strinput = input ("Input Your Sentence: ")

d = {}

for i in strinput:
    try:
        d[i] += 1
    except:
        d[i] = 1

for B in d.keys():
    print ("%s: %d" %(B, d[B]))