s = input ("Input Your Sentence: ")


lettercounts = countletters(s)
for letter,count in lettercounts.iteritems():
    print "%s=%s" % (letter, count)