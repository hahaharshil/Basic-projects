while True:
    try:
        print("To quit the program enter Q")
        #getting the number
        x = float(input("Number: "))

        #Basic framework

        a = x * 1
        b = x * 2
        c = x * 3
        d = x * 4
        e = x * 5
        f = x * 6
        g = x * 7
        h = x * 8
        i = x * 9
        j = x * 10

        #Output

        print(f'''
{x} x 1  =  {a}
{x} x 2  =  {b}
{x} x 3  =  {c}
{x} x 4  =  {d}
{x} x 5  =  {e}
{x} x 6  =  {f}
{x} x 7  =  {g}
{x} x 8  =  {h}
{x} x 9  =  {i}
{x} x 10 =  {j}     
''')
 

    except ValueError:
        print("Phele fursat mai nikal")
        break

