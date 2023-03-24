import pathlib
import random 
from string  import ascii_letters
# WORD = "SNAKE"


def main():
    
    word = get_random_word()
    
    for guess_num in range(1,7):
        guess = input(f"\nGuess a word {guess_num}: ").upper()
        show_guess(guess,word)
        if guess==word:  
            # print('Correct')
            break
    else:
        game_over(word)
        
def get_random_word(): 

    wordlist= pathlib.Path(__file__).parent/'wordlist.txt'
    words = [ 
    word.upper()
    for word in wordlist.read_text(encoding="utf-8").split('\n')
    if len(word)==5 and all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)

def show_guess(guess,word):    
    correct_letters ={
        letter for letter , correct in zip(guess,word) if letter==correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    
    wrong_letter = set(guess)-set(word)
    
    
    print('Correct leters:'," ,".join(sorted(correct_letters)))
    print('Misplaced letters:',','.join(sorted(misplaced_letters)))
    print('Wrong letter :',','.join(sorted(wrong_letter)))
    # 
def game_over(word):
     print(f'The Correct word is: {word}')
if __name__ =='__main__':
    main()