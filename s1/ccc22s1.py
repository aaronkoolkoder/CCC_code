# CCC '22 S1 - Good Fours and Good Fives
# 5/5 Aaron Merchant

n = int(input())
n2 = n
ways = 0
done = False

if n % 4 == 0:
    ways += 1
if n % 5 == 0:
    ways += 1

n2 = n - 4
while n2 > 4:
    if n2 % 5 == 0:
        done = True
        ways += 1
    n2 -= 4

if not done:
    n2 = n - 5
    while n2 > 5:
        if n2 % 4 == 0:
            ways += 1
        n2 -= 5

print(ways)
