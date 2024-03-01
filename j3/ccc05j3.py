#CCC '05 J3 - Returning Home
#5/5 Aaron Merchant

not_completed = True
directions = []
streets = []

while not_completed:
    direction = input()
    street = input()
    if street != "SCHOOL":
        directions.append(direction)
        streets.append(street)
    else:
        not_completed = False
        directions.append(direction)

directions.reverse()
streets.reverse()
streets.append("HOME")

for i in directions:
    if i == "R":
        directions[directions.index(i)] = "LEFT"
    if i == "L":
        directions[directions.index(i)] = "RIGHT"
for j in range(len(directions)):
    if streets[j] != "HOME":
        print(f"Turn {str(directions[j])} onto {str(streets[j])} street.")
    else:
        print(f"Turn {str(directions[j])} into your HOME.")
