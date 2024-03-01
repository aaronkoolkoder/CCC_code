#CCC '24 J3 - Bronze Count
#5/5 Aaron Merchant

n = int(input())
scores = [int(input()) for _ in range(n)]

scores.sort(reverse=True)
bron_sc = list(reversed(sorted(set(scores))))[2]

count = 0
for score in scores:
    if score == bron_sc:
        count += 1

print(f"{bron_sc} {count}")
