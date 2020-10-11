import random



p = 0

v = int(input("Enter times: "))
Heads = 0
Tails = 0


while p < v:
    x = random.randint(0,1)
    
    p += 1
    if x == 0:
        Heads += 1
    if x == 1:
        Tails += 1

print(f"(Heads: {Heads} , Tails: {Tails})")



