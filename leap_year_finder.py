while True:
    try:
        x = int(input('Year: '))

        if x % 4 == 0 and x != 100:
            print(f"{x} is a leap year")

        else:
            print(f"{x} is not a leap year ")

    except ValueError :
        break
