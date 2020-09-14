import random

snum = random.randint(1 , 20)

print("""
You have to guess the number between 1 and 20.
You will get chances randomly.
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░

""")



n = random.randint(4 , 10)
print(f"You got {n} chances")

while True:
    m = input("Number: ")
    if int(m) == snum:
        print("You won")
        break

    if int(m) < snum:
        n = n - 1
        print("Think big")
        if n > 1:
            print(f"You have {n} tries left")
        if n == 1:
            print(f"You have 1 try left")

    if int(m) > snum:
        n = n - 1
        print("Not that big")
        if n > 1:
            print(f"You have {n} tries left")
        if n == 1:
            print(f"You have 1 try left")

    if n == 0:
        print('You lost')
        break
