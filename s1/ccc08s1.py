# CCC '08 S1 - It's Cold Here!
# 5/5 Aaron Merchant

cities = []
temps = []

while True:
    ct = input().split(" ")
    cities.append(ct[0])
    temps.append(int(ct[1]))
    if cities[-1] == "Waterloo":
        break
ctemps = temps.index(min(temps))
print(cities[ctemps])
