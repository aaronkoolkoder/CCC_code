#CCC '22 J2 - Fergusonball Ratings
#3/3 Aaron Merchant

n = int(input())
gold_players = 0
output = ""
for i in range(n):
    points = int(input())
    fouls = int(input())
    if (points*5 - fouls*3) > 40:
        gold_players += 1
if gold_players == n:
    print(f"{gold_players}+")
else:
    print(gold_players)
