running = True

while running:
	try:
		number = input("Number: ")
		times = input("Times: ")



		for num in range(int(times) + 1):
			x = int(number) * int(num) 
			print(f"{number} x {num} =   {x} ")

    except ValueError:
    	print("Plese give a valid input")
    	break

