"""
    A deductive game whwre you must guess a number based  on cluess
    """

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(
        f"""Bagels is a deductive logic game
          
          I am thinking of a {NUM_DIGITS} digits number with no repeated digits
          Trying to guess what it is . Hre are some clues
          When i say   That means:
          Pico         One diggit is correct but in the wrong position .
          Fermi        One digit is correct and int he right postion.
          Bagels        No digit is correct """
    )

    while True:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                print("you got it ")
                break
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"the answer is {secretNum}")
            print("Do you want to play again ?(yes ,no)")
            if not input("> ").startswith("y"):
                break
            # print('THanks for playing')


def getSecretNum():
    numbers = list("123456789")
    random.shuffle(numbers)

    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        return secretNum


def getClues(guess, secretNum):
    if guess == secretNum:
        print("You got it")
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append("Fermi")
        elif guess[i] in secretNum:
            clues.append("Pico")
        # elif guess[i] not in secretNum:
        #     clues.append('Bagels for append')
    if len(clues) == 0:
        return "Bagel from if "
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
