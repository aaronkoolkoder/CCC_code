# CCC '13 S1 - From 1987 to 2013
# 5/5 Aaron Merchant
# No clue how this was a senior 1 it was ridiculously easy

y = int(input())
while True:
    y+=1
    if len(set(str(y))) == len(str(y)):
        break
print(y)
