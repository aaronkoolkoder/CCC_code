# CCC '19 J3 - Cold Compress
# 5/5 Aaron Merchant

n = int(input())

for i in range(n):
    inp = list(input())
    out = ""
    letter = inp[0]
    counts = 1

    for j in range(1, len(inp)):
        if inp[j] == inp[j - 1]:
            counts += 1
        else:
            out += f"{counts} {letter} "
            counts = 1
            letter = inp[j]

    out += f"{counts} {letter} "

    print(out)
