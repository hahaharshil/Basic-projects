import random , sys

print("Think a number between 1 and 20")
snumber = random.randint(1 , 20)
numberoftry = 6

while True:
    n = input("Number: ")

    if snumber < int(n) and numberoftry != 0:
        print("Not that big")
        numberoftry = numberoftry - 1
        print(f"{numberoftry} of tries left...")


    if snumber > int(n) and numberoftry != 0:
        print('Think big')
        numberoftry = numberoftry - 1
        print(f"{numberoftry} tries left...")


    if snumber == int(n) and numberoftry != 0:
        print("You won")
        print(f"You took {numberoftry} tries")
        break
