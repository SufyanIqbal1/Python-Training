Words = { 0 : '', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
      6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
      11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
      15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
      19 : 'ninteen', 20 : 'twenty', \
      30 : 'thirty', 40 : 'fourth', 50 : 'fifty', 60 : 'sixty', \
      70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }


num=int(input('please enter an integer between 1 and 9999: '))

def Numbers2Words(num):

    if (num < 20):
        return Words[num]

    if (num < 100):
        if num % 10 == 0:
            return Words[num]
        else:
            return Words[num // 10 * 10] + ' ' + Words[num % 10]

    if (num < 1000):
        if num % 100 == 0:
            return Words[num // 100] + ' hundred'
        else:
            return Words[num // 100] + ' hundred and ' + Numbers2Words(num % 100)
    if (num < 1000000):
        if num  == 0:
            return Numbers2Words(num // 1000) + ' thousand'
        else:
            return Numbers2Words(num // 1000) + ' thousand ' + Numbers2Words(num % 1000)

print (Numbers2Words(num))