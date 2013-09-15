# KidsCanCode - Intro to Programming
# Rock/Paper/Scissors game
import random

choices = ['r', 'p', 's']

player_wins = ['pr', 'rs', 'sp']

player_score = 0
computer_score = 0

while True:
    player_move = input("Your move? ")
    if player_move == 'q':
        break

    computer_move = random.choice(choices)

    print("You:", player_move)
    print("Me:", computer_move)

    combo = player_move + computer_move

    if player_move == computer_move:
        print("Tie!")
    elif combo in player_wins:
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

print("SCORES:")
print("You: ", player_score)
print("Me: ", computer_score)

