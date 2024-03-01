# CCC '04 J3 - Smile with Similes
# 5/5 Aaron Merchant

a = int(input())
n = int(input())

adjectives = []
nouns = []

for i in range(a):
    adjectives.append(input())
for j in range(n):
    nouns.append(input())

for k in range(a*n):
    try:
        for l in range(n):
            print(f"{adjectives[k]} as {nouns[l]}")
    except IndexError:
        pass
