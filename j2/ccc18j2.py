#CCC '18 J2 - Occupy parking
#3/3 Aaron Merchant

N=int(input())
yesterday = input()
today = input()
similar = 0
for i in range(N):
    if yesterday[i] == "C" and yesterday[i] == today[i]:
        similar+=1
print(similar)
