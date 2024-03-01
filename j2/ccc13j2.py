#CCC '13 J2 - Rotating letters
#3/3 Aaron Merchant

unaffected = ['I', 'O', 'S', 'H', 'Z', 'X', 'N']
word = input()
counter = 0
for i in range(len(word)):
    if word[i] in unaffected:
      counter +=1
if counter == len(word):
   print("YES")
else:
   print("NO")
