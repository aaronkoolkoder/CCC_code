#CCC '19 J2 - Time to Decompress
#3/3 Aaron Merchant

L = int(input())
to_print = []
for i in range(L):
    amount = input().split()
    times = int(amount[0])
    message = str(amount[1])
    print(times*message)
