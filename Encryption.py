import os

inputFilename = 'ABC.txt'
outputFilename = 'ABC.encrypted.txt'
Key = 5
Mode = 'encrypt'
	
if not os.path.exists(inputFilename):
	print('The file %s does not exist. Quitting...' % (inputFilename))
	sys.exit()
	
if os.path.exists(outputFilename):
	print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
	response = input('> ')
	if not response.lower().startswith('c'):
		sys.exit()
		
fileObj = open(inputFilename)
content = fileObj.read()
encrypted = ""
for letter in (content):
	if letter == " ":
		encrypted += " "
	else: 
		encrypted += chr(ord(letter) + 5)
fileObj.close()

print('%sing...' % (Mode.title()))

outputFileObj = open(outputFilename, 'w')
outputFileObj.write(encrypted)
outputFileObj.close()
print('Done %sing %s (%s characters).' % (Mode, inputFilename, len(content)))
print('%sed file is %s.' % (Mode.title(), outputFilename))