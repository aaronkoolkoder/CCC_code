#CCC '20 J3 - Art
#5/5 Aaron Merchant

n = int(input())
x = []
y = []
for i in range(n):
    pos = list(map(int, input().split(",")))
    x.append(pos[0])
    y.append(pos[1])
print(str(min(x)-1) + "," + str(min(y)-1))
print(str(max(x)+1) + "," + str(max(y)+1))
