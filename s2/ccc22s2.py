# CCC '22 S2 - Good Groups
# 5/5 Aaron Merchant

same_group = []
diff_group = []
point_to = {}

violations = 0

x = int(input())
for _ in range(x):
    p1, p2 = input().split()
    same_group.append([p1, p2])

y = int(input())
for _ in range(y):
    p1, p2 = input().split()
    diff_group.append([p1, p2])

g = int(input())
rounds = 1
while rounds<=g:
    p1, p2, p3 = input().split()
    for point in [p1, p2, p3]:
        point_to[point] = rounds
    rounds += 1

for p1, p2 in same_group:
    if point_to[p1] != point_to[p2]:
        violations += 1
for p1, p2 in diff_group:
    if point_to[p1] == point_to[p2]:
        violations += 1
    
print(violations)
