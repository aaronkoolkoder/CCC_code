# CCC '11 S1 - English or French?
# 5/5 Aaron Merchant

n = int(input())
list = []
s_count = 0
t_count = 0

for i in range(n):
    line = input().replace(" ", "").lower()
    list.append(line)

for element in list:
    s_count += element.count('s')
    t_count += element.count('t')

if t_count > s_count:
    print("English")
elif s_count > t_count:
    print("French")
elif s_count == t_count:
    print("French")
