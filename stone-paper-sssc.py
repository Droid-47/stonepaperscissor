import random
import sys

print("Let's Play ROCK PAPER SCISSORS GAME!")

wins = losses = ties = 0

move_names = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}
valid_moves = ['R', 'P', 'S']

while True:
    print(f"\nCurrent streak: {wins} Wins, {losses} Losses, {ties} Ties")
    playermove = input("Type 'Q' to quit | 'R' for ROCK | 'P' for PAPER | 'S' for SCISSORS: ").strip().upper()

    if playermove == 'Q':
        print("Thanks for playing! Final Score:")
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")
        sys.exit()
    if playermove not in valid_moves:
        print("Invalid input. Please choose R, P, or S.")
        continue

    print(f"{move_names[playermove]} versus...")

    compMove = random.choice(valid_moves)
    print(move_names[compMove])

    if playermove == compMove:
        print("It's a tie!")
        ties += 1
    elif (playermove == 'R' and compMove == 'S') or \
         (playermove == 'P' and compMove == 'R') or \
         (playermove == 'S' and compMove == 'P'):
        print("It's a win!")
        wins += 1
    else:
        print("It's a loss!")
        losses += 1
