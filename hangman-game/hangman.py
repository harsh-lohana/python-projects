import random
from hangman_words import word_list
from hangman_art import logo, stages
# from replit import clear
print(logo)
answer = random.choice(word_list)
word_length = len(answer)
current = []
for i in range(word_length) :
    current += "_"
print("Word =", current)
lives = 6
end_of_game = False
while not end_of_game :
    # clear()
    guess = input("Guess a letter : ").lower()
    print(guess)
    for i in range(word_length) :
        if(answer[i] == guess) :
            current[i] = guess
    if guess not in answer :
        lives -= 1
    if lives == 0 :
        end_of_game = True
        print("You LOSE!!!")
        print("Answer =", answer)
    print(current)
    print(stages[lives])
    if "_" not in current :
        end_of_game = True
        print("You WIN!!!")