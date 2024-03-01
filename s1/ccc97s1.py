#CCC '97 S1 - Sentences
#5/5 Aaron Merchant

n = int(input())

for _ in range(n):
    num_sub = int(input())
    num_verb = int(input())
    num_obj = int(input())

    subs = []
    for i in range(num_sub):
        subs.append(input())
    
    verbs = []
    for j in range(num_verb):
        verbs.append(input())

    objs = []
    for k in range(num_obj):
        objs.append(input())   
        
    
    for s in subs:
        for v in verbs:
            for o in objs:
                print(f"{s} {v} {o}.")
