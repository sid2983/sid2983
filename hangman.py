import random
import hangman_art
import hangman_words
# word_list = ["mouse","advertere","gladiator","miscellaneous","grandfather","remarkable","marvellous"]
chosen_word = random.choice(hangman_words.word_list)
display = []
lives = 6
print(hangman_art.logo+"\n")
word_len = len(chosen_word)
for i in range(word_len):
    display+="_"

guess = input("Guess a letter : ").lower()
end_of_game=False
while not end_of_game:
    for i in range(word_len):
        letter=chosen_word[i]
        if letter==guess:
            display[i]=letter
        
    print(display)
    if guess not in chosen_word:
        lives-=1
        print(f"you guessed {guess} and that's not present in the word.\n You lose a life!!")
        print(hangman_art.stages[lives])
    
    if "_" not in display:
        end_of_game=True
        print("Player has won the game")
        break
    
    elif lives == 0:
        end_of_game = True
        print("You lose")
        print(f"The correct word was {chosen_word}")
        break
    
    else:
        guess = input("guess a letter again : ").lower()
        
        
    