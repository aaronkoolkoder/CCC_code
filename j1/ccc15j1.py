#CCC '15 J1 - Special Day
#3/3 Aaron Merchant

month = int(input())
day = int(input())
if month < 2 or (month == 2 and day < 18):
    print("Before")
elif month > 2 or (month == 2 and day > 18):
    print("After")
else:
    print("Special")
