s = input ("Input Your Sentence: ")

freq = [0 for _ in range(26)]
        for letter in s:
            freq[ord(letter) - ord('a')] += 1
			
		ans = ''
        for i in range(26):
            if freq[i] + k == n:
                ans = n * chr(ord('a') + i)
                break
        return ans