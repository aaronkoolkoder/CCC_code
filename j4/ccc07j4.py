#CCC '07 J4 - Anagram Checker
#5/5 Aaron Merchant

a = input().replace(" ","").upper()
b = input().replace(" ","").upper()
if sorted(a) == sorted(b):
    print("Is an anagram.")
else:
    print("Is not an anagram.")
