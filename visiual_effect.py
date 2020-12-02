import random



p = 0

v = int(input("Enter times: "))
Heads = 0
Tails = 0


while p < v:
    x = random.randint(0,1)
    # print(x , end = "")
    p += 1
    if x == 0:
        Heads += 1
    if x == 1:
        Tails += 1

print(f"\n(Heads: {Heads} , Tails: {Tails})")


mn = Heads - Tails
nm = Tails - Heads


if Heads > Tails:
    print("Heads was geater by" , mn )

if Heads < Tails:
    print("Tails was greater by" , nm)


