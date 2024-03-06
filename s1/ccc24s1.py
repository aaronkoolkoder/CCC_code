# CCC '24 S1 - Hat Circle
# 5/5 Aaron Merchant
# 18.76 secs thru DMOJ

n = int(input())
seats = []
count = 0

for _ in range(n):
    seats.append(int(input()))

for i in range(n//2):
    opp_ind = (i + n // 2)
    if seats[i] == seats[opp_ind]:
        count+=2

print(count)
