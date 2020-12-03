import random

word = "hey"



chances = 6

tries = 6

gussed_letter = []
gussed_word = []

print("_ " * (len(word) + 1))

while tries > 0:
	guess = input("Guss the word: ").upper()
	if len(guess) == 1 and guess.isalpha():
		if guess in gussed_letter:
			print("You already tried this..")

		else guess not in word:
			print(f"{guess} not in the word...")
			tries -= 1
			print(f"{tries} tries left")
			guess.append()
		else:





	








