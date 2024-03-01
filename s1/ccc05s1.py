# CCC '05 S1 - Snow Calls
# 5/5 Aaron Merchant

dic= {'A':2, 'B':2, 'C': 2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4, 'I':4, 
      'J':5, 'K':5, 'L':5, 'M':6, 'N':6, 'O':6, 'P':7, 'Q':7, 'R':7, 
      'S':7, 'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9, 'Z':9}

t = int(input())
phones = []
outputs = []

for i in range(t):
    num = input().replace("-", "")
    phones.append(num)

for j in range(t):
    thelist = list(phones[j])
    for k in range(len(thelist)):
        if thelist[k] in dic.keys():
            thelist[k] = str(dic.get(thelist[k]))
    outputs.append(thelist)


for output in outputs:
    fir = ''.join(output[:3])
    del output[:3]
    sec = ''.join(output[:3])
    del output[:3]
    thi = ''.join(output[:4])
    print(fir + '-' + sec + '-' + thi)
