# CCC '11 S2 - Multiple Choice
# 5/5 Aaron Merchant

questions = int(input())
stu_list = []
ans_key = []
counter = 0
for i in range(questions):
    stu_list.append(input())
for j in range(questions):
    ans_key.append(input())
for k in range(questions):
    if stu_list[k] == ans_key[k]:
        counter+=1
print(counter)
