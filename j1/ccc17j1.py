#CCC '17 J1 - Quadrant Selection
#3/3 Aaron Merchant

x=int(input())
y=int(input())
a=int()

if x > 0 and y > 0:
    a=1
elif x < 0 and y > 0:
    a=2
elif x < 0 and y < 0:
    a=3
else:
    a=4

print(a)
