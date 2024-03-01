#CCC '21 J2 - Silent Auction
#3/3 Aaron Merchant

total_bids = int(input())
top_bid = 0
top_bidder = ""
for _ in range(total_bids):
    name = input()
    money = int(input())
    if money > top_bid:
        top_bid = money
        top_bidder = name
print(top_bidder)
