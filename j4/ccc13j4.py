#CCC '13 J4 - Time on task
#5/5 Aaron Merchant

t = int(input())
c = int(input())
chores = []
maxchores = 0
for i in range(c):
    chores.append(int(input()))
chores.sort()
for j in range(c):
    if chores[0] <= t:
        maxchores+=1
    else: break
    t-=chores[0]
    del chores[0]
print(maxchores)
