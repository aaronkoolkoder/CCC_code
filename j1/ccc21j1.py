#CCC '21 J1 - Boiling Water
#3/3 Aaron Merchant

B=int(input())
P=5*B-400
print(P)
if P==100:
    print("0")
elif P<100:
    print("1")
else:
    print("-1")
