from random import randint

print("\nWelcome to the Game!")
dificulty = input("Enter 'h' for HARD dificulty and 'e' for EASY dificulty : ")

lives = 10
if dificulty == 'h' :
    lives = 5

print(f"You have {lives} lives")

answer = randint(1, 100)
print("Computer has guessed a number between 1 and 100")

end_of_game = False

while not end_of_game :
    guess = int(input("Enter your guess : "))
    if guess == answer :
        end_of_game = True
        print("You WIN!!!")
    else :
        if guess < answer :
            print("Go higher!")
        else :
            print("Go lower!")
        lives -= 1
        print(f"You have {lives} lives remaining")
    if lives == 0 :
        print("You LOSE!!!")
        print(f"Computer had guessed {answer}")
        end_of_game = True