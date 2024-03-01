# CCC '17 J2 - Shifty Sum
# 3/3 Aaron Merchant

n = int(input())
k = int(input())
new = 0

for i in range(k + 1):
    new += n * 10 ** i
print(new)
