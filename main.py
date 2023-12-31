import random

print("Welcome to the word guessing game!")

words = ['giraffe', 'lion', 'tiger', 'gorilla']

currentWord = words[random.randrange(0,(len(words)-1))]

max_guesses = 3
guesses = 0

name = input("What's your name? ")
print(f"Hi {name}!")
result = '_'*len(currentWord)

while True:
    if guesses >= max_guesses:
        print("Sorry, you ran out of guesses")
        break
    print(f"{name}, the word is {result} and you have {max_guesses - guesses} guesses left")
    state = input("Do you want to guess a letter or the word? (letter/word): ")
    while True:
        if state == 'letter' or state == 'word':
            break
        else:
            state = input("Invalid input, please try again (letter/word): ")

    if state == 'letter':
        letter = input("Guess a letter: ")
        for i in range(len(currentWord)):
            if letter == currentWord[i]:
                result.replace(result[i], letter)
        print(result)
        guesses += 1

    if state == 'word':
        guess = input("What's your guess? ")
        if guess == currentWord:
            print ("Congratulations!")
            break
        else:
            print("Wrong guess, try again.")
            guesses += 1



