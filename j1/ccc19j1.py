#CCC '19 J1 - Winning Score
#3/3 Aaron Merchant 

a3 = int(input())
a2 = int(input())
a1 = int(input())
b3 = int(input())
b2 = int(input())
b1 = int(input())
ao = a3*3 + a2*2 + a1
bo = b3*3 + b2*2 + b1
if ao > bo:
    print("A")
elif bo > ao:
    print("B")
elif bo == ao:
    print("T")
