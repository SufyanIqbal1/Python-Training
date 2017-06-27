Sentence = input('Enter your Sentence To Find Consonants: ')

print("\n Consonants")
for Cons in 'bcdfghjklmnpqrstvwxyz, BCDFGHJKLMNPQRSTVWXYZ':
    if Cons in Sentence:
        print(Cons)
		

Sentence = input('Enter your Sentence To Find Vowels: ')		
print("\n VOWELS")
for Vowels in 'aeiou, AEIOU':
	if Vowels in Sentence:
		print(Vowels)
	