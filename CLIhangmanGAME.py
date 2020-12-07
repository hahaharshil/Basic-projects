import random

word = "hey"



chances = 6

tries = 6

gussed_letter = []
gussed_word = []

word_completion = ("_ " * (len(word) + 1))
print(word_completion)


while tries > 0:
	guess = input("Guss the word: ").upper()
	if len(guess) == 1 and guess.isalpha():
		if guess in gussed_letter:
			print("You already tried this..")

		elif guess not in word:
			print(f"{guess} not in the word...")
			tries -= 1
			print(f"{tries} tries left")
			guessed_letters.append(guess)
		else:
			print("Good, {guess} in the word")
			guessed_letters.append(guess)
			word_as_list = list(word_completion)
			indices = [i for i, letter in enumerate(word) if letter == guess]
			for index in indices:
			    word_as_list[index] = guess
			word_completion = "".join(word_as_list)
			if "_" not in word_completion:
			    guessed = True









	








