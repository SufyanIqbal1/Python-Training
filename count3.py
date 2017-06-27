s = input ("Input Your Sentence: ")
 
freq = [0 for _ in range(26)]
for c in s:
    freq[ord(c) - ord('a')] += 1
     
 
for i in range(len(freq)):
    cnt = freq[i]
    letter = chr( ord('a') + i )
    print(cnt, "times", letter)