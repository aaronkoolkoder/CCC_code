#CCC '09 J3 - Good Times
#5/5 Aaron Merchant

ottawa = int(input())
print(f"{ottawa} in Ottawa")
toronto = ottawa
halifax = ottawa + 100
stjohns = ottawa + 130

if ottawa < 1000:
    ottawa += 2400

victoria = ottawa - 300
edmonton = ottawa - 200
winnipeg = ottawa - 100

if victoria > 2400:
    victoria -= 2400

if edmonton > 2400:
    edmonton -= 2400

if winnipeg > 2400:
    winnipeg -= 2400

if "45" in str(ottawa):
    stjohns += 40

print(f"{victoria} in Victoria")
print(f"{edmonton} in Edmonton")
print(f"{winnipeg} in Winnipeg")
print(f"{toronto} in Toronto")
print(f"{halifax} in Halifax")
print(f"{stjohns} in St. John's")
