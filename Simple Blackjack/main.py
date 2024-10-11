import random
from random import randint

import art

dealing_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card():
    return random.choice(dealing_cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_s, computer_s):
    if player_s == computer_s:
        return "Draw"
    elif computer_s == 0:
        return "Lose, opponent has Blackjack"
    elif player_s == 0:
        return "Win with a Blackjack"
    elif player_s > 21:
        return "You went over. You lose"
    elif computer_s > 21:
        return "Opponent went over. You win"
    elif player_s > computer_s:
        return "You win"
    else:
        return "You lose"

def blackjack():
    player_hand = []
    computer_hand = []
    player_score = -1
    computer_score = -1
    continue_playing = True
    keep_drawing = True
    print(art.logo)
    while continue_playing:
        if input("Would you like to play blackjack? y/n\n") == "y":
            print("\n" * 30)
            player_hand.append(draw_card())
            player_hand.append(draw_card())
            computer_hand.append(draw_card())
            computer_hand.append(draw_card())
            player_score = calc_score(player_hand)
            computer_score = calc_score(computer_hand)
            print(f"Your Cards: {player_hand}, current score: {player_score}")
            print(f"Dealer's first card: {computer_hand[0]}")
            while keep_drawing:
                if input("Get another card? y/n\n" == "y"):
                    player_hand.append(draw_card())
                    print(f"Your Cards: {player_hand}, current score: {player_score}")
                else:
                    keep_drawing = False

            while computer_score != 0 and computer_score < 17:
                computer_hand.append(draw_card())
                computer_score = calc_score(computer_hand)

            print(f"Your Final Cards: {player_hand}, Final score: {player_score}")
            print(f"Dealers Final Cards: {computer_hand}, Final score: {computer_score}")
            print(compare(player_score, computer_score))
        else:
            print("Have a nice day!")
            continue_playing = False

blackjack()