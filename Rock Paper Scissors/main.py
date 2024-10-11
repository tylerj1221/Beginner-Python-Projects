import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
computerRoll = random.randint(0, 2)
playerRoll = int(input("Rock, paper, scissors? 0, 1, 2\n"))
print("Player Roll: " + game_images[playerRoll])
print("Computer Roll: " + game_images[computerRoll])

if playerRoll >= 3 or playerRoll < 0:
    print("You typed an invalid number. You lose!")
elif playerRoll == 0 and computerRoll == 2:
    print("You win!")
elif computerRoll == 0 and playerRoll == 2:
    print("You lose!")
elif computerRoll > playerRoll:
    print("You lose!")
elif playerRoll > computerRoll:
    print("You win!")
elif computerRoll == playerRoll:
    print("It's a draw!")
