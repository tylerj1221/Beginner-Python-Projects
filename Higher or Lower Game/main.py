import game_data
import art
import os
import random

data = game_data.data

def generate_players():
    player1 = data[random.randint(0, len(data) - 1)]
    player2 = data[random.randint(0, len(data) - 1)]
    if player2 == player1:
        player2 = data[random.randint(0, len(data) - 1)]
    players = [player1, player2]
    return players

def more_followers_a_or_b(players):
    if players[0]["follower_count"] > players[1]["follower_count"]:
        return "a"
    else:
        return "b"

def higher_lower_game():
    score = 0
    keep_playing = True
    while keep_playing:
        os.system('cls')
        print(art.logo)
        if score > 0:
            print(f"Correct!\nCurrent Score: {score}")
        players = generate_players()
        higher_followers = more_followers_a_or_b(players)
        print(f"Compare A: {players[0]['name']}, a {players[0]['description']}, from {players[0]['country']}")
        print(art.vs)
        print(f"Compare B: {players[1]['name']}, a {players[1]['description']}, from {players[1]['country']}")
        if input("Who has more followers? A or B?\n").lower() == higher_followers:
            score += 1
        else:
            keep_playing = False
    os.system('cls')
    print(art.logo)
    print(f"That's incorrect! Final Score: {score}")

higher_lower_game()