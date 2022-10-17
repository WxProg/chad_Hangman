# All modules needed throuhgout the program
import random
import hangman_words as hw
import hangman_art as ha
from replit import clear

# List of all variables used within program.
word_list = hw.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []
already_guessed = []

#Game Intro
print(ha.logo)
print("\nA man was wrongfully convicted and is about to be hanged.")
print("Can you get him the justice he deserves?\n")

for _ in range(word_length):
    display += "_"
print(f"Hint: The word contains {len(display)} letters.")
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    #Inform the user, letter is already guessed.
    if guess in already_guessed:
        print("Letter is already guessed. Guess again!")
    else:
        already_guessed +=  guess
    #Loops through chosen word and display letter if guess is correct.    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter         
    #Check if user guess in not in chosen word and inform the user they lost a life.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("He was hangeg. May his blood rest on your shoulders!")
            print(f"The word was:{chosen_word} ")

    #Join all the elements in the list and concatenate into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters. If so, end game.
    if "_" not in display:
        end_of_game = True
        print("Well done. He will have a fair trial!")

    print(ha.stages[lives])