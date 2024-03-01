#CCC '16 J1 - Tournament Selection
#3/3 Aaron Merchant

wins = 0
losses = 0
for _ in range(6):
    question = input("")
    if "W" in question:
        wins += 1
if wins == 5 or wins == 6:
    print("1")
elif wins == 3 or wins == 4:
    print("2")
elif wins == 1 or wins == 2:
    print("3")
else:
    print("-1")
