# CCC '14 J3 - Double Dice
# 5/5 Aaron Merchant

Antonia = 100
David = 100
rolls = int(input())
for _ in range(rolls):
    the_roll = input().split()
    a = int(the_roll[0])
    d = int(the_roll[1])
    if a > d:
        David-=a
    elif d > a:
        Antonia-=d
print(Antonia)
print(David)
