import random
import art

def guessing_game():
    print(art.logo)
    lives = -1
    player_guess = -1
    guessing_number = random.randint(0, 100)
    game_running = True
    print("Beginning the number guessing game!")
    if input("What difficulty would you like? Easy or Hard?\n").lower() == "hard":
        lives = 5
    else:
        lives = 10

    while game_running:
        print(f"You have {lives} lives")
        player_guess = int(input("Guess a number\n"))

        if player_guess > guessing_number:
            print("Too High!")
            lives -= 1
        elif player_guess < guessing_number:
            print("Too Low!")
            lives -= 1
        elif player_guess == guessing_number:
            print("You guessed correctly!")
            game_running = False
            if input("Play Again? y/n\n").lower() == "y":
                print("\n" * 20)
                guessing_game()
        else:
            print("Incorrect Input! -1 life")
            lives -= 1

guessing_game()