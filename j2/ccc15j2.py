#CCC '15 J2 - Happy or Sad
#3/3 Aaron Merchant

emotion = str(input())

h = emotion.count(':-)')
s = emotion.count(':-(')

if h > s:
    print("happy")
elif s > h:
    print("sad")
elif h == 0 and s == 0:
    print("none")
else:
    print("unsure")
