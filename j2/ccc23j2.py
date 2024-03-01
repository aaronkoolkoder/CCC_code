#CCC '23 J2 - Chili Peppers
#3/3 Aaron Merchant

values = {
    'Poblano' : 1500,
    'Mirasol' : 6000,
    'Serrano' : 15500,
    'Cayenne' : 40000,
    'Thai' : 75000,
    'Habanero' : 125000
}
O = 0
N = int(input(""))

for _ in range(N):
    pepper_name = input().strip()
    O += values[pepper_name]
print(O)
