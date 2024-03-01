# CCC '12 S2 - Aromatic Numbers
# ?/5 Aaron Merchant

# Only did half of the question lol
# Work in Progress...

aromatic = input()
arabic = ''.join([char for char in aromatic if char.isdigit()])
roman = ''.join([char for char in aromatic if char.isalpha()])
values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
total = 0
for i in range(len(arabic)):
    total += int(arabic[i]) * values.get(roman[i])
print(total)
