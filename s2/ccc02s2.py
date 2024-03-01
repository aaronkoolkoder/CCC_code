# CCC '02 S2 - Fraction Action
# 40/180 Aaron Merchant
# No clue why it doesnt work
# I asked some friends on why and they had no clue either

numerator = int(input())
denominator = int(input())

a, b = numerator, denominator
while b:
    a, b = b, a % b

simplified_numerator = numerator // a
simplified_denominator = denominator // a

whole_part = simplified_numerator // simplified_denominator
remainder = simplified_numerator % simplified_denominator

if remainder == 0:
    print(whole_part)
else:
    print(f"{whole_part} {remainder}/{simplified_denominator}")
